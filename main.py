#!/usr/bin/env python3
"""
Cybersecurity Toolkit - Main Entry Point
A professional ethical hacking toolkit for penetration testing and security analysis.

WARNING: This toolkit is for educational and ethical purposes only.
Unauthorized use against systems without permission is illegal.
"""

import sys
import os
import argparse
from tools import port_scanner, brute_force, subdomain_finder, header_analyzer, packet_sniffer
from utils import logger, helpers

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("      CYBERSECURITY TOOLKIT")
    print("      Ethical Hacking Tools")
    print("="*50)
    print("1. Port Scanner")
    print("2. Password Brute Force Simulator")
    print("3. Subdomain Finder")
    print("4. HTTP Header Analyzer")
    print("5. Network Sniffer")
    print("6. Exit")
    print("="*50)

def main():
    """Main function to run the toolkit."""
    parser = argparse.ArgumentParser(description="Cybersecurity Toolkit")
    parser.add_argument('--gui', action='store_true', help='Run with GUI interface')
    args = parser.parse_args()

    if args.gui:
        # Import and run GUI
        try:
            from gui import run_gui
            run_gui()
        except ImportError:
            print("GUI module not available. Install required dependencies.")
            sys.exit(1)
    else:
        # CLI Mode
        while True:
            display_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == '1':
                target = input("Enter target IP: ").strip()
                port_range = input("Enter port range (e.g., 1-1024 or 'full'): ").strip()
                results = port_scanner.run(target, port_range)
                if results:
                    print("Open ports:")
                    for port, service in results:
                        print(f"  {port}: {service}")
                else:
                    print("No open ports found.")
            elif choice == '2':
                target_url = input("Enter login URL: ").strip()
                username = input("Enter username: ").strip()
                wordlist = input("Enter password wordlist path: ").strip()
                result = brute_force.run(target_url, username, wordlist)
                if result:
                    print(f"Password found: {result}")
                else:
                    print("No password found.")
            elif choice == '3':
                domain = input("Enter domain: ").strip()
                wordlist = input("Enter subdomain wordlist path: ").strip()
                results = subdomain_finder.run(domain, wordlist)
                if results:
                    print("Found subdomains:")
                    for sub in results:
                        print(f"  {sub}")
                else:
                    print("No subdomains found.")
            elif choice == '4':
                url = input("Enter URL: ").strip()
                headers, issues = header_analyzer.run(url)
                if headers:
                    print("Headers:")
                    for key, value in headers.items():
                        print(f"  {key}: {value}")
                    if issues:
                        print("Security issues:")
                        for issue in issues:
                            print(f"  - {issue}")
                else:
                    print("Failed to retrieve headers.")
            elif choice == '5':
                interface = input("Enter network interface (optional): ").strip() or None
                duration = int(input("Enter duration in seconds: ").strip() or 10)
                results = packet_sniffer.run(interface, duration)
                if results:
                    print("Captured packets:")
                    for packet in results:
                        print(f"  {packet}")
                else:
                    print("No packets captured.")
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()