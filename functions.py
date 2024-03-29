import os
import socket
import platform
import subprocess
import cpuinfo
import yaml
import csv
from datetime import datetime


class Config:
    def __init__(self, current_directory=None, config_path=None, server_name=None, serverName_noSpace=None,
                 textFilePath=None, credential_path=None, workbook=None, worksheet=None, region=None, location=None,
                 drive_bays=None, connection_type=None):
        self.current_directory = current_directory
        self.config_path = config_path
        self.server_name = server_name
        self.serverName_noSpace = serverName_noSpace
        self.textFilePath = textFilePath
        self.credential_path = credential_path
        self.workbook = workbook
        self.worksheet = worksheet
        self.location = location
        self.region = region
        self.drive_bays = drive_bays
        self.connection_type = connection_type

    def __str__(self):
        return (f"Current Directory: {self.current_directory}")

    def set_current_directory(self, current_directory):
        self.current_directory = current_directory

    def set_config_path(self, config_path):
        self.config_path = config_path

    def set_credential_path(self, credential_path):
        self.credential_path = credential_path

    def set_server_name(self, server_name):
        self.server_name = server_name

    def set_workbook(self, workbook):
        self.workbook = workbook

    def set_worksheet(self, worksheet):
        self.worksheet = worksheet

    def set_region(self, region):
        self.region = region

    def set_location(self, location):
        self.location = location

    def set_drive_bays(self, drive_bays):
        self.drive_bays = drive_bays

    def set_connection_type(self, connection_type):
        self.connection_type = connection_type

    def __call__(self):
        # Print all the attributes
        print(f"Current Directory: {self.current_directory}, Configuration Path: {self.config_path}, Server Name Space: {self.server_name}, Server Name No space: {self.serverName_noSpace}, "
              f"Text File Path: {self.textFilePath}, API Credential Path: {self.credential_path}, Workbook: {self.workbook}, Worksheet: {self.worksheet}, Region: {self.region}, Drive Bays:"
              f"{self.drive_bays}, Connection Type: {self.connection_type}")


class Server:
    def __init__(self, name=None, ip=None, username=None, operating_system=None, cpu=None, product_name=None,
                 product_version=None, drives=None, hyperlink=None):
        self.name = name
        self.ip = ip
        self.username = username
        self.operating_system = operating_system
        self.cpu = cpu
        self.product_name = product_name
        self.product_version = product_version
        self.drives = drives
        self.hyperlink = hyperlink

    def __str__(self):
        return (f"Server: {self.name}, IP: {self.ip}, Username: {self.username}, OS: {self.operating_system}, "
                f"CPU: {self.cpu}")

    def __call__(self):
        # Print all the attributes
        print(f"Server: {self.name}, IP: {self.ip}, Username: {self.username}, "
              f"OS: {self.operating_system}, CPU: {self.cpu}, Product Name: {self.product_name}, "
              f"Product Version: {self.product_version}, Drives: {self.drives}")

    # Add Name to the server object
    def set_name(self, name):
        self.name = name

    # Add IP address to the server object
    def add_ip(self, ip):
        self.ip = ip

    # Add Username to the server object
    def add_username(self, username):
        self.username = username

    # Add Operating System to the server object
    def add_operating_system(self, operating_system):
        self.operating_system = operating_system

    # Add CPU to the server object
    def add_cpu(self, cpu):
        self.cpu = cpu

    # Add Product Name to the server object
    def add_product_name(self, product_name):
        self.product_name = product_name

    # Add Product Version to the server object
    def add_product_version(self, product_version):
        self.product_version = product_version

    def set_drives(self, drives):
        self.drives = drives

    def set_hyperlink(self, hyperlink):
        self.hyperlink = hyperlink


# Retrieve Username of the user
def get_username():
    username = "Unknown"
    try:
        if os.name == 'nt':
            username = os.getenv('username')
        elif os.name == 'posix':
            username = os.getenv('USER')

    except Exception as e:
        print(str(e) + "Error getting username!")

    return username


# Get local IP address
def get_ip():
    ip = "Unknown"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.0.0.0", 0))
        ip = s.getsockname()[0]
        s.close()
    except Exception as e:
        print(str(e) + "Error getting IP address!")
    return ip


# Get Operating System
def get_os():
    operating_system = "Unknown"
    try:
        # Get Specific OS
        if os.name == 'nt':
            operating_system = platform.platform(terse=True)
            return operating_system
        elif os.name == 'posix':
            RELEASE_DATA = {}
            with open("/etc/os-release") as f:
                reader = csv.reader(f, delimiter="=")
                for row in reader:
                    if row:
                        RELEASE_DATA[row[0]] = row[1]

            if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
                with open("/etc/debian_version") as f:
                    DEBIAN_VERSION = f.readline().strip()
                major_version = DEBIAN_VERSION.split(".")[0]
                version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
                if version_split[0] == major_version:
                    # Just major version shown, replace it with the full version
                    RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])

            OS = "{} {}".format(RELEASE_DATA["NAME"], RELEASE_DATA["VERSION"])
            return OS

    # Needs to be fixed
            #operating_system = platform.platform(terse=True)
            #return operating_system

    except Exception as e:
        print(str(e) + "Error getting Operating System!")
    return operating_system


# Get CPU info
def get_cpu():
    cpu = "Unknown"
    try:
        cpu = cpuinfo.get_cpu_info()['brand_raw']
    except Exception as e:
        print(str(e) + "Error getting CPU info!")
    return cpu


# Get System Product Name
def get_product_name():
    product_name = "Unknown"
    try:
        if os.name == 'nt':
            product_name = subprocess.check_output('wmic csproduct get name').decode().split('\n')[1].strip()
            return product_name
        elif os.name == 'posix':
            product_name = subprocess.check_output('cat /sys/class/dmi/id/product_name', shell=True).decode().strip()
            return product_name
    except Exception as e:
        print(str(e) + "Error getting Product Name!")
    return product_name


# Get System Product Version
def get_product_version():
    product_version = "Unknown"
    try:
        if os.name == 'nt':
            product_version = subprocess.check_output('wmic csproduct get version').decode().split('\n')[1].strip()
            #print("Here")
            return product_version
        elif os.name == 'posix':
            product_version = subprocess.check_output('cat /sys/class/dmi/id/product_version', shell=True).decode().strip()
            return product_version

    except Exception as e:
        print(str(e) + "Error getting Product Version!")

    return product_version


# Get Folder Where Script is Located
def get_current_directory():
    current_directory = "Unknown"
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
    except Exception as e:
        print(str(e) + "Error getting current directory!")
    return current_directory


# Get Path of Config File
def get_config_path(main_directory):
    config_path = "Unknown"
    try:
        config_path = os.path.join(main_directory, 'config.yaml')
    except Exception as e:
        print(str(e) + "Error getting config path!")
    return config_path


# Get Path of Credentials File
def get_credential_path(config_path):
    credentials_path = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            credential_name = config['credentialsName']
            # Extract the directory from the config_path
            config_directory = os.path.dirname(config_path)
            # Join the directory path with the credential file name
            credentials_path = os.path.join(config_directory, credential_name)
    except Exception as e:
        print(str(e) + "Error getting credentials path!")
    return credentials_path


# Get Server Name
def get_server_name(config_path):
    server_name = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            server_name = config['serverName']
    except Exception as e:
        print(str(e) + "Error getting server name!")
    return server_name


# Get Workbook Name
def get_workbook(config_path):
    workbook = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            workbook = config['workBook']
    except Exception as e:
        print(str(e) + "Error getting workbook name!")
    return workbook


# Get Worksheet Name
def get_worksheet(config_path):
    worksheet = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            worksheet = config['workSheet']
    except Exception as e:
        print(str(e) + "Error getting worksheet name!")
    return worksheet


# Get Region
def get_region(config_path):
    region = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            region = config['region']
    except Exception as e:
        print(str(e) + "Error getting region!")
    return region

def get_location(config_path):
    location = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            location = config['location']
    except Exception as e:
        print(str(e) + "Error getting location!")
    return location

# Get Drive Bays
def get_drive_bays(config_path):
    drive_bays = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            drive_bays = config['driveBays']
    except Exception as e:
        print(str(e) + "Error getting drive bays!")
    return drive_bays


# Get Connection Type
def get_connection_type(config_path):
    connection_type = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            connection_type = config['connectionType']
    except Exception as e:
        print(str(e) + "Error getting connection type!")
    return connection_type


# Get Time
def get_time():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")


# Get Drive information
def get_drives():
    drives = []

    try:
        if os.name == 'posix':
            result = subprocess.Popen(['lsblk', '-d', '-n', '-o', 'MODEL,NAME,SIZE,TYPE'], stdout=subprocess.PIPE)
            result = result.communicate()[0].decode().split('\n')
            for drive in result:
                if drive:
                    try:
                        drives.append(drive)
                    except Exception as e:
                        print(str(e))

        elif os.name == 'nt':
            result = subprocess.run(['wmic', 'diskdrive', 'get', 'model,name,size'], stdout=subprocess.PIPE)
            result = result.stdout.decode().split('\n')
            for drive in result[1:]:
                if drive:
                    try:
                        size = drive.strip().split()[-1]
                        size = str(int(size) // (10**9))
                        drive_string = drive.strip().split()[:-1]
                        drive_string = " ".join(drive_string)
                        drive_string += "\t" + size + " GB"
                        drives.append(drive_string)
                    except Exception as e:
                        print(str(e))
        return drives

    except Exception as e:
        print(str(e) + "Error getting drive info!")


# Get Hyperlink
def get_hyperlink(server_name):
    hyperlink = "Unknown"
    # remove spaces from server name
    server_name_plus = server_name.replace(" ", "+")
    try:
        hyperlink = '=HYPERLINK("https://npsg-wiki.elements.local/display/~pashmore/' + server_name_plus + '", "' + server_name + '")'
    except Exception as e:
        print(str(e) + "Error getting hyperlink!")
    return hyperlink