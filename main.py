from functions import *


def retrieve_server_info(server):
    server()
    server.add_ip(get_ip())
    server.add_username(get_username())
    server.add_operating_system(get_os())
    server.add_cpu(get_cpu())
    server.add_product_name(get_product_name())
    server.add_product_version(get_product_version())
    server()


if __name__ == '__main__':
    server = Server()
    retrieve_server_info(server)
