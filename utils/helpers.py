#!/usr/bin/env python3
"""
Helper Utilities
Common functions for the toolkit.
"""

import ipaddress

def validate_ip(ip):
    """Validate IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_url(url):
    """Basic URL validation."""
    return url.startswith(('http://', 'https://'))

def format_results(results, tool_name):
    """Format results for display or saving."""
    output = f"=== {tool_name.upper()} RESULTS ===\n"
    if isinstance(results, list):
        for item in results:
            output += str(item) + '\n'
    elif isinstance(results, dict):
        for key, value in results.items():
            output += f"{key}: {value}\n"
    else:
        output += str(results) + '\n'
    return output