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

def retrieve_config_values(config):
    config()

    config.set_current_directory(get_current_directory())
    config.set_config_path(get_config_path(config.current_directory))
    config.set_credential_path(get_credential_path(config.config_path))

    config.set_server_name(get_server_name(config.config_path))
    config()

if __name__ == '__main__':
    #server = Server()
    config = Config()
    print(config)
    retrieve_config_values(config)
    #retrieve_server_info(server)
