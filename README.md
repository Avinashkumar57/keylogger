# Key Logger in Python

## Overview

This Python Key Logger is a simple program that records keystrokes on a user's machine. It can be used for educational purposes to understand how keylogging works, or to monitor usage on a personal device. 

**Disclaimer:** This project is intended for educational purposes only. Unauthorized use of keyloggers may violate privacy laws and ethical guidelines. Always ensure you have permission before monitoring any device.

## Features

- Captures all keystrokes in real-time
- Logs keystrokes to a file
- Supports customizable logging intervals
- Lightweight and easy to use

## Prerequisites

- Python 3.x
- Required libraries (listed below)
  1.import logging
  2.import smtplib
  3.import threading
  4.import os
  5.import shutil
  6.from datetime import datetime
  7.import pyscreenshot
  8.from pynput import keyboard
  9.from pynput.mouse import Listener, Button
 10.from email.mime.multipart import MIMEMultipart
 11.from email.mime.text import MIMEText
 12.from email.mime.base import MIMEBase
 13.from email import encoders

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

## Usage

1. Open the terminal or command prompt.
2. Run the keylogger script:
   ```bash
   python keylogger.py
   ```
3. The keylogger will start capturing keystrokes and saving them to `log.txt`.

### Stopping the Key Logger

To stop the keylogger, simply terminate the script (e.g., using `Ctrl + C` in the terminal).

## Configuration

You can customize the following parameters in `keylogger.py`:

- **log_file**: Change the name of the log file.
- **logging_interval**: Set how often to log the keystrokes (in seconds).

## Example Log Output

The log file (`log.txt`) will contain all captured keystrokes in the order they were typed. Each keypress will be recorded on a new line.

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the existing style and includes appropriate documentation.

## Acknowledgments

- [Pynput](https://pypi.org/project/pynput/) for handling keyboard events in Python.

## Contact

For questions or inquiries, feel free to reach out:

- Email: your.email@example.com
- GitHub: [Avinashkumar57](https://github.com/Avinashkumar57)

---

**Note:** Please use this tool responsibly and ethically.






