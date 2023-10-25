import os


# Retrieve Username of the user
def get_username():
    username = "Unknown"

    # Windows
    if os.name == 'nt':
        username = os.getenv('username')
        print("Windows!")

    # Linux
    elif os.name == 'posix':
        username = os.getenv('USER')
        print("Linux!")

    return username
