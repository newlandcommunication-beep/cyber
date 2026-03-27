#!/usr/bin/env python3
"""
Network Sniffer Module
Captures and analyzes network packets.
"""

from scapy.all import sniff, IP, TCP, UDP
from utils import logger
import threading
import time

class PacketSniffer:
    def __init__(self, interface=None):
        self.interface = interface
        self.packets = []
        self.running = False

    def packet_callback(self, packet):
        """Callback for each captured packet."""
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
            info = f"Source: {src} -> Destination: {dst} | Protocol: {proto}"
            self.packets.append(info)
            logger.log_info(info)

    def start_sniffing(self, count=0):
        """Start sniffing packets."""
        self.running = True
        logger.log_info(f"Starting packet sniffing on interface {self.interface or 'default'}")
        sniff(iface=self.interface, prn=self.packet_callback, count=count, stop_filter=lambda x: not self.running)

    def stop_sniffing(self):
        """Stop sniffing."""
        self.running = False
        logger.log_info("Stopped packet sniffing.")

def run(interface=None, duration=10):
    """Run packet sniffer."""
    sniffer = PacketSniffer(interface)
    sniffer_thread = threading.Thread(target=sniffer.start_sniffing)
    sniffer_thread.start()
    time.sleep(duration)
    sniffer.stop_sniffing()
    sniffer_thread.join()
    return sniffer.packets