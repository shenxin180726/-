from socket import *
from multiprocessing import Process
from signal import *
server_addr = ("0.0.0.0",8888)
def handle():
    pass
def main():
    sockfd = socket()
    sockfd.bind(server_addr)
    sockfd.listen(5)
    signal(SIGCHLD,SIG_IGN)
    while True:
        try:
            connfd,addr = sockfd.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            print("服务结束")
            break
        p = Process(target=handle,args=(connfd,))
        p.daemon = True
        p.start()
    sockfd.close()
if __name__ == '__main__':
    main()







