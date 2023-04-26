import socket
import sys
import threading

if len(sys.argv) != 2:
    print("Usage: python port_scanner.py <IP address>")
    sys.exit(1)

target = sys.argv[1]

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    if result == 0:
        service_name = get_service_name(port)
        print(f"Port {port} ({service_name}) is open")
    s.close()

def get_service_name(port):
    try:
        service = socket.getservbyport(port)
        return service
    except OSError:
        return "unknown"

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()