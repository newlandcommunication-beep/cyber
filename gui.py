#!/usr/bin/env python3
"""
GUI Dashboard for Cybersecurity Toolkit
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import threading
import time
from tools import port_scanner, brute_force, subdomain_finder, header_analyzer, packet_sniffer
from utils import helpers
import io
import sys

class CyberToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Toolkit - GUI Dashboard")
        self.root.geometry("800x600")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.create_port_scanner_tab()
        self.create_brute_force_tab()
        self.create_subdomain_tab()
        self.create_header_analyzer_tab()
        self.create_sniffer_tab()

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_port_scanner_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Port Scanner")

        # Inputs
        ttk.Label(tab, text="Target IP:").grid(row=0, column=0, padx=5, pady=5)
        self.port_target = ttk.Entry(tab)
        self.port_target.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Port Range:").grid(row=1, column=0, padx=5, pady=5)
        self.port_range = ttk.Entry(tab)
        self.port_range.insert(0, "1-1024")
        self.port_range.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(tab, text="Scan", command=self.run_port_scan).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(tab, text="Export", command=lambda: self.export_results(self.port_results, "port_scan")).grid(row=2, column=1, padx=5, pady=5)

        # Results
        self.port_results = scrolledtext.ScrolledText(tab, height=20)
        self.port_results.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_brute_force_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Brute Force")

        ttk.Label(tab, text="Login URL:").grid(row=0, column=0, padx=5, pady=5)
        self.bf_url = ttk.Entry(tab)
        self.bf_url.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Username:").grid(row=1, column=0, padx=5, pady=5)
        self.bf_user = ttk.Entry(tab)
        self.bf_user.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Wordlist:").grid(row=2, column=0, padx=5, pady=5)
        self.bf_wordlist = ttk.Entry(tab)
        self.bf_wordlist.insert(0, "wordlists/passwords.txt")
        self.bf_wordlist.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Run", command=self.run_brute_force).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(tab, text="Export", command=lambda: self.export_results(self.bf_results, "brute_force")).grid(row=3, column=1, padx=5, pady=5)

        self.bf_results = scrolledtext.ScrolledText(tab, height=20)
        self.bf_results.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_subdomain_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Subdomain Finder")

        ttk.Label(tab, text="Domain:").grid(row=0, column=0, padx=5, pady=5)
        self.sub_domain = ttk.Entry(tab)
        self.sub_domain.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Wordlist:").grid(row=1, column=0, padx=5, pady=5)
        self.sub_wordlist = ttk.Entry(tab)
        self.sub_wordlist.insert(0, "wordlists/subdomains.txt")
        self.sub_wordlist.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Find", command=self.run_subdomain_finder).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(tab, text="Export", command=lambda: self.export_results(self.sub_results, "subdomains")).grid(row=2, column=1, padx=5, pady=5)

        self.sub_results = scrolledtext.ScrolledText(tab, height=20)
        self.sub_results.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_header_analyzer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Header Analyzer")

        ttk.Label(tab, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        self.header_url = ttk.Entry(tab)
        self.header_url.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Analyze", command=self.run_header_analyzer).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(tab, text="Export", command=lambda: self.export_results(self.header_results, "headers")).grid(row=1, column=1, padx=5, pady=5)

        self.header_results = scrolledtext.ScrolledText(tab, height=20)
        self.header_results.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_sniffer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Network Sniffer")

        ttk.Label(tab, text="Interface:").grid(row=0, column=0, padx=5, pady=5)
        self.sniff_interface = ttk.Entry(tab)
        self.sniff_interface.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Duration (s):").grid(row=1, column=0, padx=5, pady=5)
        self.sniff_duration = ttk.Entry(tab)
        self.sniff_duration.insert(0, "10")
        self.sniff_duration.grid(row=1, column=1, padx=5, pady=5)

        self.start_sniff_btn = ttk.Button(tab, text="Start Sniffing", command=self.start_sniffing)
        self.start_sniff_btn.grid(row=2, column=0, padx=5, pady=5)
        self.stop_sniff_btn = ttk.Button(tab, text="Stop", command=self.stop_sniffing, state=tk.DISABLED)
        self.stop_sniff_btn.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Export", command=lambda: self.export_results(self.sniff_results, "packets")).grid(row=3, column=0, padx=5, pady=5)

        self.sniff_results = scrolledtext.ScrolledText(tab, height=20)
        self.sniff_results.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.sniffing = False

    def run_port_scan(self):
        target = self.port_target.get()
        port_range = self.port_range.get()
        if not target or not port_range:
            messagebox.showerror("Error", "Please enter target and port range")
            return
        self.status_var.set("Scanning ports...")
        threading.Thread(target=self._port_scan_thread, args=(target, port_range)).start()

    def _port_scan_thread(self, target, port_range):
        results = port_scanner.run(target, port_range)
        self.port_results.delete(1.0, tk.END)
        for port, service in results:
            self.port_results.insert(tk.END, f"Port {port}: {service}\n")
        self.status_var.set("Port scan complete")

    def run_brute_force(self):
        url = self.bf_url.get()
        user = self.bf_user.get()
        wordlist = self.bf_wordlist.get()
        if not url or not user or not wordlist:
            messagebox.showerror("Error", "Please fill all fields")
            return
        self.status_var.set("Running brute force...")
        threading.Thread(target=self._brute_force_thread, args=(url, user, wordlist)).start()

    def _brute_force_thread(self, url, user, wordlist):
        result = brute_force.run(url, user, wordlist)
        self.bf_results.delete(1.0, tk.END)
        if result:
            self.bf_results.insert(tk.END, f"Password found: {result}\n")
        else:
            self.bf_results.insert(tk.END, "No password found\n")
        self.status_var.set("Brute force complete")

    def run_subdomain_finder(self):
        domain = self.sub_domain.get()
        wordlist = self.sub_wordlist.get()
        if not domain or not wordlist:
            messagebox.showerror("Error", "Please enter domain and wordlist")
            return
        self.status_var.set("Finding subdomains...")
        threading.Thread(target=self._subdomain_thread, args=(domain, wordlist)).start()

    def _subdomain_thread(self, domain, wordlist):
        results = subdomain_finder.run(domain, wordlist)
        self.sub_results.delete(1.0, tk.END)
        for sub in results:
            self.sub_results.insert(tk.END, f"{sub}\n")
        self.status_var.set("Subdomain discovery complete")

    def run_header_analyzer(self):
        url = self.header_url.get()
        if not url:
            messagebox.showerror("Error", "Please enter URL")
            return
        self.status_var.set("Analyzing headers...")
        threading.Thread(target=self._header_thread, args=(url,)).start()

    def _header_thread(self, url):
        headers, issues = header_analyzer.run(url)
        self.header_results.delete(1.0, tk.END)
        if headers:
            for key, value in headers.items():
                self.header_results.insert(tk.END, f"{key}: {value}\n")
            if issues:
                self.header_results.insert(tk.END, "\nSecurity Issues:\n")
                for issue in issues:
                    self.header_results.insert(tk.END, f"- {issue}\n")
        self.status_var.set("Header analysis complete")

    def start_sniffing(self):
        interface = self.sniff_interface.get()
        duration = int(self.sniff_duration.get() or 10)
        self.sniffing = True
        self.start_sniff_btn.config(state=tk.DISABLED)
        self.stop_sniff_btn.config(state=tk.NORMAL)
        self.status_var.set("Sniffing packets...")
        threading.Thread(target=self._sniff_thread, args=(interface, duration)).start()

    def stop_sniffing(self):
        self.sniffing = False
        self.start_sniff_btn.config(state=tk.NORMAL)
        self.stop_sniff_btn.config(state=tk.DISABLED)
        self.status_var.set("Sniffing stopped")

    def _sniff_thread(self, interface, duration):
        # For real-time, we'll simulate by updating periodically
        start_time = time.time()
        while self.sniffing and time.time() - start_time < duration:
            # In real implementation, integrate with sniffer
            self.sniff_results.insert(tk.END, f"Simulated packet at {time.time()}\n")
            self.sniff_results.see(tk.END)
            time.sleep(1)
        self.stop_sniffing()

    def export_results(self, text_widget, default_name):
        content = text_widget.get(1.0, tk.END)
        if not content.strip():
            messagebox.showwarning("Warning", "No results to export")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name,
                                                filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")])
        if file_path:
            if file_path.endswith('.pdf'):
                try:
                    from reportlab.pdfgen import canvas
                    from reportlab.lib.pagesizes import letter
                    c = canvas.Canvas(file_path, pagesize=letter)
                    width, height = letter
                    y = height - 40
                    for line in content.split('\n'):
                        if y < 40:
                            c.showPage()
                            y = height - 40
                        c.drawString(40, y, line)
                        y -= 15
                    c.save()
                    messagebox.showinfo("Success", f"Results exported to PDF: {file_path}")
                except ImportError:
                    messagebox.showerror("Error", "reportlab not installed. Install with: pip install reportlab")
            else:
                with open(file_path, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Success", f"Results exported to TXT: {file_path}")

def run_gui():
    root = tk.Tk()
    app = CyberToolkitGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()