#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.google.com", 80))
s.sendall(("GET / HTTP/1.1\r\n\r\n").encode())
print(s.recv(4096))
s.close()
