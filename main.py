from functions import *


def method_name():
    server.name = "Server 1"
    server.ip = get_ip()
    server.username = get_username()
    server.operating_system = get_os()
    server.cpu = get_cpu()


if __name__ == '__main__':
    server = Server()
    # Print
    print(server)
    print(get_product_name())
    print(get_product_version())

    # Call functions and fill in the server object
    method_name()

    # Print
    print(server)
