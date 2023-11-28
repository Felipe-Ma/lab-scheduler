from functions import *
import logging
import pygsheets

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def retrieve_server_info(server):
    server()
    logging.info("Retrieving server info")
    server.add_ip(get_ip())
    server.add_username(get_username())
    server.add_operating_system(get_os())
    server.add_cpu(get_cpu())
    server.add_product_name(get_product_name())
    server.add_product_version(get_product_version())
    logging.info("Server info retrieved")
    server()


def retrieve_config_values(config):
    config()
    logging.info("Retrieving config values")
    config.set_current_directory(get_current_directory())
    config.set_config_path(get_config_path(config.current_directory))
    config.set_credential_path(get_credential_path(config.config_path))
    config.set_workbook(get_workbook(config.config_path))
    config.set_worksheet(get_worksheet(config.config_path))
    config.set_region(get_region(config.config_path))
    config.set_drive_bays(get_drive_bays(config.config_path))
    config.set_connection_type(get_connection_type(config.config_path))
    config.set_server_name(get_server_name(config.config_path))
    logging.info("Config values retrieved")
    config()


def insert_pygsheets(config, server):
    logging.info("Attempting to connect to Google Sheets")
    gc = pygsheets.authorize(service_file=config.credential_path)
    logging.info("Connected to Google Sheets")

    # Practice batch update
    logging.info("Attempting to batch update")
    sh = gc.open(config.workbook)
    wks = sh.worksheet_by_title(config.worksheet)

    # Update server name
    wks.update_value('B1', server.name)
    data = [
        #["Data1", "Data2", "Data3"], # First row
        #["Data4", "Data5", "Data6"], # Second row
        #[server.name],

    ]

    #.update_values(crange='A1', values=data)

if __name__ == '__main__':
    server = Server()
    config = Config()
    logging.info("Created server and config objects")

    retrieve_config_values(config)
    retrieve_server_info(server)

    server.set_name(config.server_name)
    server()

    insert_pygsheets(config, server)
