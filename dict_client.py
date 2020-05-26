"""
dict 客户端
收集请求，发送请求，获取结果，展示
"""
from socket import *
server_addr = ("127.0.0.1",8888)
#搭建服务链接
def main():
    sockfd = socket()
    sockfd.connect(server_addr)

if __name__ == '__main__':
    main()
