import socket
import threading
from my_protobuf import example_pb2


class MySocket(object):

    def __init__(self, ip, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__ip = ip
        self.__port = port
        self.__socket.bind((ip, port))

    # 开始监听请求
    def listening(self):
        self.__socket.listen(20)  # 最大连接数
        print('Waiting for connection...')
        t = threading.Thread(target=MySocket.loop_recv, args=(self,))
        t.start()

    # 循环等待客户端连解
    def loop_recv(self):
        while True:
            # 接受一个新连接:
            sock, addr = self.__socket.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(
                target=MySocket.handle_client_socket,
                args=(self, sock, addr))
            t.start()

    # 客户端已连解到服务端
    def handle_client_socket(self, sock, addr):
        print('New Client Connect to Server, Address is', addr)
        # 循环监听客户端的请求，赶时间，不做分包粘包异步处理
        while True:
            data = sock.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                continue
            t = threading.Thread(target=MySocket.handle_client_request, args=(self, data))
            t.start()

    # 处理客户端发送过来的数据
    def handle_client_request(self, data):
        target = example_pb2.all_person()
        target.ParseFromString(data)
        print('client send data:%s %s', 
        (target.Per[0].name, target.Per[1].name))

            
                































    # def __init__(self, ip, port):
    #     self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.__ip = ip
    #     self.__port = port

    
    # def connect(self):
    #     self.__socket.connect((self.__ip, self.__port))


    # def send(self, msg):
    #     self.__socket.send(msg)


    # def recv(self, msg):
    #     self.__socket

    