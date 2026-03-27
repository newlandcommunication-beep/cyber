#!/usr/bin/env python3
"""
Subdomain Finder Module
Discovers subdomains using wordlist.
"""

import requests
from concurrent.futures import ThreadPoolExecutor
from utils import logger

def check_subdomain(domain, subdomain):
    """Check if subdomain exists."""
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code < 400:
            return f"{subdomain}.{domain}"
    except:
        pass
    return None

def run(domain, wordlist_path, max_threads=50):
    """Run subdomain discovery."""
    logger.log_info(f"Starting subdomain discovery for {domain}")

    try:
        with open(wordlist_path, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.log_error(f"Wordlist file not found: {wordlist_path}")
        return

    found = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(check_subdomain, domain, sub) for sub in subdomains]
        for future in futures:
            result = future.result()
            if result:
                found.append(result)
                logger.log_info(f"Found subdomain: {result}")

    logger.log_info(f"Discovery complete. Found {len(found)} subdomains.")
    return found