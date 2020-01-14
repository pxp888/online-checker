import socket
import threading
import time
import datetime
import pytz

def human(t):
    # lt = time.localtime(t)
    # n = str(lt[0]) + '-'+ str(lt[1]) +'-'+ str(lt[2]) + ' ' + str(lt[3]) + ':' + str(lt[4])
    a = datetime.datetime.fromtimestamp(t)
    b = a.astimezone(pytz.timezone("Asia/Manila"))
    n = b.strftime("%y-%m-%d %H:%M")
    return str(n)


class serv(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('starting watcher')
        UDP_IP = "0.0.0.0"
        UDP_PORT = 8889

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

        while True:
            data, addr = self.sock.recvfrom(1024)
            data = data.decode('utf-8')
#            print('recv : ',data)
            lock.acquire()
            if data in lc:
                t = time.time() - lc[data]
                if t > cut:
                    n = str(data) + ' | ' + human(lc[data]) + ' | '+ human(time.time()) + '\n'
                    fil = open('gaps.txt','a')
                    fil.write(n)
                    fil.close()
                    print('gap',data,t,human(lc[data]))
            lc[data] = time.time()
            lock.release()


class thing(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('starting checker')
        old = ''
        onlinea = ''
        onlineb = ''
        while True:
            n = ''
            onlinea = ''
            lock.acquire()
            for i in lc:
                t = time.time() - lc[i]
                if t > cut:
                    n = n + str(i) +'  ' + human(lc[i]) + '\n'
                    #print('miss',i,human(lc[i]))
                else:
                    onlinea = onlinea + str(i) + ', '
            lock.release()

            if not onlinea==onlineb:
                print('online', human(time.time()))
                print(onlinea)
            onlineb = onlinea

            if not n==old:
                fil = open('missing.txt','w')
                fil.write(n)
                fil.close()
                print('miss')
                print(n)
            old = n
            time.sleep(1)

lock = threading.Lock()
cut = 45
lc = {}

wat = serv()
wat.start()
x = thing()
x.start()

wat.join()
x.join()
