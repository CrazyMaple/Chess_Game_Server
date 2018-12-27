

import socket
import time
from my_protobuf import example_pb2


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    print('create client socket, connect to server')
    s.connect(('127.0.0.1', 6666))
    pers = example_pb2.all_person()
    p1 = pers.Per.add()
    p1.id = 1
    p1.name = (str.format(
        'client connect time i'
        's %s' % time.strftime("%Y-%m-%d %X", time.localtime())))
    p2 = pers.Per.add()
    p2.id = 2
    p2.name = 'crazymaple'
    s.send(pers.SerializeToString())
    s.close()


if __name__ == "__main__":
    main()

# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()