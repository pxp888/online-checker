import socket
import time

UDP_IP = "52.193.85.143"
# UDP_IP = "127.0.0.1"
UDP_PORT = 8889
MESSAGE = "ubu"

def ping():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
    try:
        ping()
    except:
        pass
    time.sleep(10)
