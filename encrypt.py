import os 
import sys 
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv('.env')

def encrypt(msg):
    key = os.getenv('KEY').encode()
    fernet = Fernet(key)
    return fernet.encrypt(msg.encode())

def decrypt(code):
    key = os.getenv('KEY').encode()
    fernet = Fernet(key)
    return fernet.decrypt(code).decode()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        password = sys.argv[1]
    else:
        password = input('Enter password to encrypt: ')
    crypt = encrypt(password)
    print(f'Encrypted Password is: ',crypt)