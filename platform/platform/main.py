

from my_socket import mysocket


def main():
    print("you fucker")
    server_socket = mysocket.MySocket('127.0.0.1', 6666)
    server_socket.listening()
    while True:
        i = 0

if __name__ == "__main__":
    main()
