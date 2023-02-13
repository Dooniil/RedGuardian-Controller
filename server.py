from singleton_decorator import singleton
import socket


@singleton
class Server:
    def __init__(self, port):
        self.__HOST_NAME = '127.0.0.1'
        self.__PORT = port
        self.__server = None

    def open_server(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.__HOST_NAME, self.__PORT))
        self.__server.listen()

    def __accept_connection(self):
        client, address = self.__server.accept()
        if client:
            print('Connected')
        return client

    def get_data(self):
        client = self.__accept_connection()
        data = client.recv(1024)
        print(data.decode('UTF-8'))


if __name__ == '__main__':
    server = Server(8999)
    server.open_server()

    while True:
        server.get_data()