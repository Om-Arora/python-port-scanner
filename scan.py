#! /usr/bin/env python3
import socket # To connect to the target
import sys # To get the ip address of the target from command line

# Check if ip address is provided
if len(sys.argv) < 2:
    print ("Ip address of target not provided !")
    print ("Usage: ./scan.py <ip-address-of-target>")
    quit()

ip = sys.argv[1]

# Do a connect scan on every port on the target machine
for port in range(1,65535):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print (f"The port {port} is open")
    except KeyboardInterrupt:
        quit()
    except:
        pass
