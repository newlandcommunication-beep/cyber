# Cybersecurity Toolkit

A professional, modular ethical hacking toolkit for penetration testing and security analysis.

## ⚠️ Disclaimer

This toolkit is intended for **educational and ethical purposes only**. Unauthorized use against systems without explicit permission is illegal and unethical. Always obtain written consent before performing security assessments.

## Features

### Core Modules

1. **Port Scanner**
   - Scan target IP addresses for open ports
   - Supports custom port ranges (1-1024 or full range)
   - Multithreaded scanning for improved performance
   - Service identification for common ports

2. **Password Brute Force Simulator**
   - Educational simulation of dictionary attacks
   - Supports custom password wordlists
   - Attempt logging and success detection

3. **Subdomain Finder**
   - Discover subdomains using wordlist-based enumeration
   - Concurrent HTTP requests for efficiency
   - Validation of discovered subdomains

4. **HTTP Header Analyzer**
   - Comprehensive header analysis
   - Security vulnerability detection
   - Checks for missing security headers (CSP, HSTS, etc.)

5. **Network Sniffer**
   - Real-time packet capture and analysis
   - Protocol detection (TCP, UDP, etc.)
   - Suspicious traffic pattern identification

### Advanced Features

- **GUI Dashboard**: Modern Tkinter-based interface with real-time monitoring
- **Export Reports**: Save results to TXT files (PDF support with reportlab)
- **Logging System**: Timestamped logs with colored CLI output
- **Modular Architecture**: Easily extensible tool structure

## Installation

### Prerequisites

- Python 3.7+
- Windows/Linux/macOS

### Setup

1. Clone or download the repository:
   ```bash
   git clone https://github.com/yourusername/cybersecurity-toolkit.git
   cd cybersecurity-toolkit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. For network sniffing (requires admin privileges):
   - Windows: Run as Administrator
   - Linux/macOS: Use `sudo`

## Usage

### CLI Mode (Default)

Run the toolkit in command-line mode:

```bash
python main.py
```

Navigate through the interactive menu to select and configure tools.

### GUI Mode

Launch the graphical dashboard:

```bash
python main.py --gui
```

The GUI provides an intuitive interface with tabs for each tool, real-time monitoring, and export capabilities.

### Command-Line Arguments

- `--gui`: Launch GUI dashboard instead of CLI

## Project Structure

```
cyber_toolkit/
│
├── main.py                 # CLI entry point
├── gui.py                  # GUI dashboard
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── tools/                 # Core security tools
│   ├── __init__.py
│   ├── port_scanner.py
│   ├── brute_force.py
│   ├── subdomain_finder.py
│   ├── header_analyzer.py
│   └── packet_sniffer.py
│
├── utils/                 # Utility modules
│   ├── __init__.py
│   ├── logger.py
│   └── helpers.py
│
└── wordlists/             # Default wordlists
    ├── passwords.txt
    └── subdomains.txt
```

## Tool Explanations

### Port Scanner
Uses socket programming to perform TCP SYN scans. Implements multithreading for concurrent port checking, significantly reducing scan time. Identifies services using the socket library's service database.

### Password Brute Force Simulator
Demonstrates dictionary attack principles. Reads passwords from a file and attempts login via HTTP POST requests. Includes rate limiting and error handling for educational purposes.

### Subdomain Finder
Performs DNS enumeration by attempting to resolve subdomains from a wordlist. Uses concurrent requests to check HTTP accessibility, filtering out invalid subdomains.

### HTTP Header Analyzer
Inspects HTTP response headers for security best practices. Checks for presence of critical security headers and flags potential vulnerabilities.

### Network Sniffer
Leverages Scapy for packet capture and analysis. Monitors network interfaces for traffic patterns, identifying source/destination IPs and protocols.

## Security Concepts Used

- **Port Scanning**: Understanding network service enumeration
- **Brute Force Attacks**: Password security and attack prevention
- **Subdomain Enumeration**: DNS reconnaissance techniques
- **Header Analysis**: Web application security headers
- **Packet Analysis**: Network traffic monitoring and intrusion detection

## Example Usage

### Port Scanning
```bash
# In CLI mode, select option 1
Target IP: 192.168.1.1
Port Range: 1-1024
```

### GUI Dashboard
1. Launch with `python main.py --gui`
2. Select "Port Scanner" tab
3. Enter target IP and port range
4. Click "Scan"
5. View results in the text area
6. Export results using "Export TXT"

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your tool/module following the existing structure
4. Update documentation
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name] - Penetration Tester & Security Researcher

## Acknowledgments

- Built with Python's security and networking libraries
- Inspired by professional penetration testing frameworks
- Educational tool for cybersecurity learning