import keyring
from getpass import getpass

def set_pass():
    login = input("Please input full email address: ")
    password = getpass()

    keyring.set_password("scraper", login, password)

    return login
