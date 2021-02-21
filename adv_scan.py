from threading import *
from socket import *
import optparse


def connection_scan(ip, port):
    try:
        con_sock = socket(AF_INET, SOCK_STREAM)
        con_sock.connect((ip, port))
        print(f"[*] {port}/TCP Port is OPEN in {ip}")
    except:
        print(f"[*] {port}/TCP Port is CLOSE in {ip}")
    finally:
        con_sock.close()


def PortScan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print("The program cannot resolve target host or else it is not reachable !")
    try:
        target_name = gethostbyaddr(target_ip)
        print(f"[*] Scan Results for : {target_name[0]}")
    except:
        print(f"[*] Scan Results for : {target_ip}")

    setdefaulttimeout(1)

    for target_port in target_ports:
        t = Thread(target=connection_scan, args=(target_host, int(target_port)))
        t.start()


def main():
    parser = optparse.OptionParser("Usage of Program: " + "-H <target host> -p <target port>")
    parser.add_option("-H", dest="target_host", type="string", help="Target Host")
    parser.add_option("-p", dest="target_port", type="string", help="Target Port")
    (options, args) = parser.parse_args()
    target_host = options.target_host
    target_ports = str(options.target_port).split(",")

    if target_host == None or target_ports[0] == None:
        print(parser.usage)
        exit(0)
    PortScan(target_host, target_ports)


if __name__ == '__main__':
    main()
