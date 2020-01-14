from pynput.mouse import Button, Controller
from pynput import keyboard
import socket
import threading
import time



mouse = Controller()

# current = {}

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))
    if key == keyboard.Key.f15:
        mouse.press(Button.left)
    if key == keyboard.Key.f16:
        mouse.press(Button.middle)
    if key == keyboard.Key.f17:
        mouse.press(Button.right)

    m = 20
    if key == keyboard.Key.f18:
        mouse.move(0,-m)
    if key == keyboard.Key.f19:
        mouse.move(-m,0)
    if key == keyboard.Key.f20:
        mouse.move(0,m)
    if key == keyboard.Key.f13:
        mouse.move(m,0)

    # try:
    #     current[str(key)] = 1
    #     k = sorted(current.keys())
    #     print(len(current))
    #     if k==["'1'", "'2'", "'3'"]: lighton()
    #     if k==["'4'", "'5'", "'6'"]: lightoff()
    # except:
    #     pass

def on_release(key):
#    print('{0} released'.format(key))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False
    if key == keyboard.Key.f15:
        mouse.release(Button.left)
    if key == keyboard.Key.f16:
        mouse.release(Button.middle)
    if key == keyboard.Key.f17:
        mouse.release(Button.right)

    # try:
    #     del current[str(key)]
    # except:
    #     pass


print('Key monitoring starting')
# Collect events until released


class cat(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                UDP_IP = "52.193.85.143"
                UDP_PORT = 8889
                MESSAGE = b'dtop'
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            except:
                pass
            time.sleep(10)


if __name__=='__main__':
    puller = cat()
    puller.start()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    puller.join()
