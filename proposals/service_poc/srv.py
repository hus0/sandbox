#!/usr/bin/python

import sys
import socket

IP = '0.0.0.0'
PORT = 5555
RECV_DATA_LEN = 1024
BACKLOG = 5

def start_srv(ip, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conn.bind((ip, port))
    print 'Listening on {0}:{1}'.format(ip, port)
    conn.listen(BACKLOG)

    while True:
        curr_conn, addr = conn.accept()
        while True:
            data = curr_conn.recv(RECV_DATA_LEN)

            if data == 'quit\r\n':
                curr_conn.close()
                break
            elif data == 'stop\r\n':
                curr_conn.close()
                sys.exit(0)
            elif data:
                curr_conn.send(data)
                print data

if __name__ == "__main__":
    try:
        try:
            ip = sys.argv[1]
            port = int(sys.argv[2])
        except IndexError:
            ip = IP
            port = PORT
        finally:
            start_srv(ip, port)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception, exc:
        print "Error occurred: %s" %exc
        sys.exit(2)
