from functions import *
import logging
import pygsheets
import time

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(log_path, "lab-scheduler.log")
logging.basicConfig(filename=log_path, filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def retrieve_server_info(server):
    #server()
    logging.info("Retrieving server info")
    server.add_ip(get_ip())
    server.add_username(get_username())
    server.add_operating_system(get_os())
    server.add_cpu(get_cpu())
    server.add_product_name(get_product_name())
    server.add_product_version(get_product_version())
    server.set_drives(get_drives())
    logging.info("Server info retrieved")
    #server()


def retrieve_config_values(config):
    #config()
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
    #config()


def insert_pygsheets(config, server):
    logging.info("Attempting to connect to Google Sheets")
    gc = pygsheets.authorize(service_file=config.credential_path)
    logging.info("Connected to Google Sheets")

    # Open workbook and worksheet
    logging.info("Opening workbook and worksheet")
    sh = gc.open(config.workbook)
    wks = sh.worksheet_by_title(config.worksheet)
    logging.info("Opened workbook and worksheet")

    # Batch update
    logging.info("Creating batch update list")
    logging.info(server.hyperlink)
    column_b = [
        [server.name, server.hyperlink, config.region, server.product_name, server.cpu, server.operating_system, config.connection_type,
         config.drive_bays],
        [],
        [config.region],
        [server.ip],
        [server.product_name + " " + server.product_version],
        [server.cpu],
        [server.operating_system],
        [config.connection_type],
        [config.drive_bays],
        [server.username],
        [get_time()]
    ]
    # Clears any prior drive data
    for i in range(0, 24):
        if i < len(server.drives):
            column_b.append([server.drives[i]])
        else:
            column_b.append([""])

    logging.info("Batch update list created")

    logging.info("Batch updating server information")
    wks.update_values(crange='B1', values=column_b)
    logging.info("Server information updated")

    return wks


def update_time_drive_pygsheets(config, server, wks):
    logging.info("Updating server drive information")
    server.set_drives(get_drives())

    logging.info("Creating batch update list")
    column_b = [
        [get_time()]
    ]

    # Clears any prior drive data
    for i in range(0, 24):
        if i < len(server.drives):
            column_b.append([server.drives[i]])
        else:
            column_b.append([""])

    logging.info("Batch update list created")

    logging.info("Batch updating server information")
    wks.update_values(crange='B11', values=column_b)
    logging.info("Server information updated")


if __name__ == '__main__':
    start_time = time.time()
    server = Server()
    config = Config()
    logging.info("Created server and config objects")

    retrieve_config_values(config)
    retrieve_server_info(server)

    server.set_name(config.server_name)
    server.set_hyperlink(get_hyperlink(config.server_name))
    #server()

    wks = insert_pygsheets(config, server)

    logging.info("Initial Sheets Update completed in %s seconds" % (time.time() - start_time))

    logging.info("Going to sleep for 1 minute")
    # Go to sleep for 1 Minute
    time.sleep(60)



    # Update the Last Updated Time and Drive Information in Pygsheets every minute
    while True:
        try:
            start_time = time.time()
            update_time_drive_pygsheets(config, server, wks)
            logging.info("Ping and Drive Update completed in %s seconds" % (time.time() - start_time))
        except Exception as e:
            logging.error(e)
            logging.error("Error updating drive information")
        time.sleep(60)
