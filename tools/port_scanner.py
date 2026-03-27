#!/usr/bin/env python3
"""
Port Scanner Module
Scans target IP for open ports and identifies services.
"""

import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from utils import logger

# Common ports and services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP"
}

def scan_port(target, port, timeout=1):
    """Scan a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = COMMON_PORTS.get(port, "Unknown")
            sock.close()
            return port, service
        sock.close()
    except Exception as e:
        logger.log_error(f"Error scanning port {port}: {e}")
    return None

def run(target, port_range, max_threads=100):
    """Run port scan."""
    logger.log_info(f"Starting port scan on {target} with range {port_range}")

    if port_range == 'full':
        ports = range(1, 65536)
    else:
        try:
            start, end = map(int, port_range.split('-'))
            ports = range(start, end + 1)
        except:
            logger.log_error("Invalid port range format. Use 'start-end' or 'full'")
            return []

    open_ports = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in ports]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
                logger.log_info(f"Port {result[0]} open: {result[1]}")

    logger.log_info(f"Scan complete. Found {len(open_ports)} open ports.")
    return open_ports