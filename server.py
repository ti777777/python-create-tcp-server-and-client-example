import socket
import threading



def start_server():
    client_id=0
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((socket.gethostname(), 8222))
    # become a server socket
    serversocket.listen(5)
    

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server

        print("client connected")
        ct = client_thread(clientsocket,client_id)
        
        ct.run()
        client_id +=1
        

class client_thread(threading.Thread):
    def __init__(self, sock, id):
        threading.Thread.__init__(self)
        self.sock =sock 
        self.id = id
    def run(self):
        print("client thread started!")
        print("I'm client{0}".format(self.id))

if __name__ == '__main__':
    start_server()