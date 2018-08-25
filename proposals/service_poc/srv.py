#!/usr/bin/python

import socket

IP = '0.0.0.0'
PORT = 5555
RECV_DATA_LEN = 1024

def listen():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conn.bind((IP, PORT))
    print 'Listening on {0}:{1}'.format(IP, PORT)
    conn.listen(10)

    while True:
        curr_conn, address = conn.accept()
        while True:
            data = curr_conn.recv(RECV_DATA_LEN)

            if data == 'quit\r\n':
                curr_conn.shutdown(1)
                curr_conn.close()
                break
            elif data == 'stop\r\n':
                curr_conn.shutdown(1)
                curr_conn.close()
                exit()
            elif data:
                curr_conn.send(data)
                print data

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
