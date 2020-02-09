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
        data = conn.rec (BUFFER_SIZE)
        if not data: break
        #print("received data:", data)
        response = bytes("HTTP/1.1 200 OK\n"
         +"Content-Type: text/html\n"
         +"\n", "utf-8")
        conn.send(response)
        with open("./python-server/index.html", "rb") as f:
            #conn.send(f.read())
            conn.sendfile(f)
        conn.close()
        #conn.send(response)