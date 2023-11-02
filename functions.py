import os
import socket
import platform
import subprocess
import cpuinfo


class Server:
    def __init__(self, name=None, ip=None, username=None, operating_system=None, cpu=None, product_name=None, product_version=None):
        self.name = name
        self.ip = ip
        self.username = username
        self.operating_system = operating_system
        self.cpu = cpu
        self.product_name = product_name
        self.product_version = product_version

    def __str__(self):
        return f"Server: {self.name}, IP: {self.ip}, Username: {self.username}, OS: {self.operating_system}, CPU: {self.cpu}"

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

    # When Server object is called, print the following
    def __call__(self):
        print(f"Server: {self.name}, IP: {self.ip}, Username: {self.username}, OS: {self.operating_system}, CPU: {self.cpu}")


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
        operating_system = platform.system()
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
            print("Here")
            return product_version
        elif os.name == 'posix':
            product_version = subprocess.check_output('cat /sys/class/dmi/id/product_version', shell=True).decode().strip()
            return product_version

    except Exception as e:
        print(str(e) + "Error getting Product Version!")

    return product_version





    return product_name

