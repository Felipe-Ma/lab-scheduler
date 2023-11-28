import yaml
import os


def storeConfig():
    # Get the folder where this script is located
    folder_path = os.path.dirname(os.path.realpath(__file__))

    current_directory = folder_path
    #current_directory = '/home/intel/Desktop/testingEnvironment/server-scheduler/'
    # Using os.path.join to create paths in a platform-independent manner
    config_path = os.path.join(current_directory, 'config.yaml')

    # Load configurations to config variable
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Store server_name
    serverName_Space = config['serverName']
    serverName_noSpace = serverName_Space.replace(" ", "")

    # Store WorkBook and WorkSheet Name
    workBook = config['workBook']
    workSheet = config['workSheet']

    # Store Region
    region = config['region']

    # store API Credentials
    apiCredential = config['credentialsName']
    apiCredentialPath = os.path.join(current_directory, apiCredential)

    # Store Text File Directory
    textFilePath = os.path.join(current_directory, serverName_noSpace + ".txt")

    # Store Drive Bays
    driveBays = config['driveBays']

    # Store Connection Type
    connectionType = config['connectionType']

    return current_directory, config_path, serverName_Space, serverName_noSpace, textFilePath, apiCredentialPath, workBook, workSheet, region, driveBays, connectionType


def printConfig(current_directory, config_path, serverName_Space, serverName_noSpace, textFilePath, apiCredentialPath,
                workBook, workSheet, region):
    print("Current Directory: " + current_directory)
    print("Configuration Path: " + config_path)
    print("Server Name Space: " + serverName_Space)
    print("Server Name No space: " + serverName_noSpace)
    print("Text File Path: " + textFilePath)
    print("API Credential Path: " + apiCredentialPath)
    print("Workbook: " + workBook)
    print("Worksheet: " + workSheet)
    print("Region: " + region)

storeConfig()

if __name__ == '__main__':
    storeConfig()
    printConfig()
