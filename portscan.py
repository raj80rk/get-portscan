import socket
import termcolor
import concurrent.futures
import time
import pyfiglet

# Display banner
banner = pyfiglet.figlet_format("Portscan")
print(termcolor.colored(banner, 'green'))
sub_banner = "Powered by eagle_rock"
print(termcolor.colored(sub_banner, 'yellow') + "\n")

# Dictionary to map port numbers to their common services
port_descriptions = {
    20: 'FTP (Data)', 21: 'FTP (Control)', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
    53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 3389: 'RDP'
}

def scan_port(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.1)
            if sock.connect_ex((ipaddress, port)) == 0:
                if port in port_descriptions:
                    port_description = port_descriptions[port]
                    print(f"[+] Port {port} ({port_description}) is open on {ipaddress}")
    except socket.error as e:
        print(f"Error: {e}")

def scan(target):
    print('\n' + f"Starting Scan For {target}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        for port in port_descriptions.keys():
            executor.submit(scan_port, target, port)

targets = input("[*] Enter Targets To Scan (split them by ,): ").split(',')
start_time = time.time()

for target in targets:
    scan(target.strip())

end_time = time.time()
print("Time Taken:", end_time - start_time)