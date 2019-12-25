import socket

def connect_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8222))


if __name__ == '__main__':
    connect_server()