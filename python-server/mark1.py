#!/usr/bin/env python3

import socket

HOST = ''
PORT = 8000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

BUFFER_SIZE = 1024


while True:    
    conn, addr = s.accept()

    print('Connection address:', addr)

    while True:
        data = conn.recv(BUFFER_SIZE)
        data = bytes("Hello There!")
        if not data: break
        print("received data:", data)
        conn.send(data)