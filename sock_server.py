import socket
import socket
from gpio_contrlol import cell_open

def runserver():
    while True:
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('172.16.1.10',65432)) #Creating socket
        print ('Socket created \n' ) 

        server.listen(5)  # Now wait for client connection.
        print('Server listening.... \n')

        client_socket, address=server.accept() #Accepting client

        cell_id=client_socket.recv(8).decode('utf-8') #Decoding client's data pull (card id)
        cell_open(cell_id,15)

        client_socket.send(b"Success")
 
runserver()
 


