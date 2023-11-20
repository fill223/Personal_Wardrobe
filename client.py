
import socket


def client(gpio_pin,ip):

    HOST = "172.16.1."  # The server's hostname or IP address
    PORT = 65432  # The port used by the server
    HOST= HOST+str(ip)
    print(HOST)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(gpio_pin.encode('utf-8'))


# import socket

# gpio_pin="7"

# HOST = "172.16.1.12"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server
# print(HOST)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(gpio_pin.encode('utf-8'))


