import socket

socket_scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_scan.settimeout(3)
ip = "192.168.0.1"


def scan_now(port):
    if socket_scan.connect_ex((ip, port)):
        print(f"{port} port is closed")
    else:
        print(f"{port} port is opened")


for i in range(100, 1, -2):
    scan_now(i)

