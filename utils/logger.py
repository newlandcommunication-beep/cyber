#!/usr/bin/env python3
"""
Logger Utility
Handles logging for the toolkit.
"""

import datetime
import colorama
from colorama import Fore, Style

colorama.init()

def log_info(message):
    """Log info message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.BLUE}[INFO {timestamp}]{Style.RESET_ALL} {message}")

def log_success(message):
    """Log success message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.GREEN}[SUCCESS {timestamp}]{Style.RESET_ALL} {message}")

def log_warning(message):
    """Log warning message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.YELLOW}[WARNING {timestamp}]{Style.RESET_ALL} {message}")

def log_error(message):
    """Log error message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.RED}[ERROR {timestamp}]{Style.RESET_ALL} {message}")

def save_to_file(filename, content):
    """Save content to file."""
    with open(filename, 'a') as f:
        f.write(content + '\n')