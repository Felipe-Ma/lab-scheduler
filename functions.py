import os
import socket
import platform


class Server:
    def __init__(self, name, ip, username):
        self.name = name
        self.ip = ip
        self.username = username


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
