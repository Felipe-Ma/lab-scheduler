from functions import *


def retrieve_server_info(server):
    server()
    server.add_ip(get_ip())
    
    server()


if __name__ == '__main__':
    server = Server()
    retrieve_server_info(server)
    # Print
    #print(server)
    #print(get_product_name())
    #print(get_product_version())

    # Call functions and fill in the server object
    #method_name()

    # Print
    #print(server)
