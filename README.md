# get-portscan
# Porscan

Porscan is a Python-based port scanning tool designed to efficiently scan network hosts and identify open ports along with their common services. This tool leverages multithreading to perform scans quickly, even across a large range of ports.

## Features

- **Fast and Efficient**: Utilizes multithreading to speed up the scanning process, making it capable of scanning a full range of ports (0-65,535) swiftly.
- **Port Descriptions**: Provides common service names for well-known ports.
- **Custom Banner**: Displays an eye-catching ASCII art banner at the start of the scan.
- **Concurrent Scanning**: Capable of scanning multiple targets concurrently.
- **User-Friendly**: Simple command-line interface for specifying target hosts and port ranges.

## Installation

To use Porscan, you need Python installed on your system along with a few additional packages. You can install the required packages using pip:

```bash
pip install termcolor pyfiglet
git clone https://github.com/raj80rk/get-portscan
cd get-portscan


