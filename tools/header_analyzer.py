#!/usr/bin/env python3
"""
HTTP Header Analyzer
Analyzes website headers for security issues.
"""

import requests
from utils import logger

SECURITY_HEADERS = {
    'Content-Security-Policy': 'Missing CSP',
    'Strict-Transport-Security': 'Missing HSTS',
    'X-Frame-Options': 'Missing X-Frame-Options',
    'X-Content-Type-Options': 'Missing X-Content-Type-Options',
    'Referrer-Policy': 'Missing Referrer-Policy',
    'Permissions-Policy': 'Missing Permissions-Policy'
}

def analyze_headers(headers):
    """Analyze headers for security issues."""
    issues = []
    for header, issue in SECURITY_HEADERS.items():
        if header not in headers:
            issues.append(issue)
    return issues

def run(url):
    """Run header analysis."""
    logger.log_info(f"Analyzing headers for {url}")

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        logger.log_info("Response Headers:")
        for key, value in headers.items():
            logger.log_info(f"{key}: {value}")

        issues = analyze_headers(headers)
        if issues:
            logger.log_warning("Security Issues Found:")
            for issue in issues:
                logger.log_warning(f"- {issue}")
        else:
            logger.log_success("All basic security headers present.")

        return headers, issues
    except Exception as e:
        logger.log_error(f"Error analyzing headers: {e}")
        return None, []