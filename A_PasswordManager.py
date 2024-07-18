import os
import subprocess
import sys

def cls():
    os.system('clear')

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

def check_packages():
    try:
        system = subprocess.run(["uname"], capture_output=True, text=True).stdout.strip()

        if "Darwin" in system:
            subprocess.run(['brew', 'install', 'sqlite3'], check=True)
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'cryptography'], check=True)

        elif "Linux" in system:
            subprocess.run(['sudo', 'apt-get', 'install', 'sqlite3', '-y'], check=True)
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'cryptography'], check=True)

        elif sys.platform == "win32":
            subprocess.run(['pip', 'install', 'pysqlite3'], check=True)
            subprocess.run(['pip', 'install', 'cryptography'], check=True)

        else:
            print(f"Cannot find this operating system to install python packages: {system}")

    except Exception as e:
        print(f"Error during the python packages installation: {str(e)}")

def show_services():
    conn.execute('SELECT service FROM credentials')
    input()
    main()

def show_database():
    input_service2 = input('Service to gain the password from: ')
    cursor.execute("SELECT * FROM credentials WHERE service=?", (input_service2,))
    row = cursor.fetchone()
    key = load_key()
    if row:
        decrypted_password = decrypt_text(row[2], key)
        print(f"Service: {input_service2}, Username: {row[1]}, Password: {decrypted_password}")
    else:
        print("No service found")
    conn.close()

def insert_credentials():
    cursor.execute('''CREATE TABLE IF NOT EXISTS credentials
                      (service TEXT, username TEXT, password TEXT)''')
    key = load_key()
    input_service = input('Service for the password: ')
    input_username = input('Username for the password: ')
    password = input('Password for the service to encrypt: ')
    encrypted_password = encrypt_text(password, key)

    cursor.execute("INSERT INTO credentials (service, username, password) VALUES (?, ?, ?)",
                   (input_service, input_username, encrypted_password))
    conn.commit()

def get_key():
    token = Fernet.generate_key()
    with open('token.txt', 'wb') as token_file:
        token_file.write(token)
    input(print(f"Your new key has been saved to token.txt: {token.decode()}"))
    dir = os.getcwd
    input('Be aware of not loosing the file, put it also in this directory when you want to access your database: {dir}')
    cls()
    main()

def load_key():
    with open('token.txt', 'rb') as token_file:
        loaded_key = token_file.read()
    return loaded_key

def main():
    while True:
        print('''Password Manager:
        
[1] Get a new Key
[2] Import your Key and show Database
[3] Import Service, Username, Password
[4] Show memorized Services
[5] Exit
''')
        input1 = input('Choose an option: ')

        if input1 == '1':
            get_key()
        elif input1 == '2':
            show_database()
        elif input1 == '3':
            insert_credentials()
        elif input1 == '4':
            show_services()
        elif input1 == '5':
            sys.exit()
        else:
            print('Error choosing option')
            cls()

if __name__ == "__main__":
    try:
        import sqlite3
        from cryptography.fernet import Fernet
    except ImportError:
        check_packages()
    conn = sqlite3.connect('Password_dB.db')
    cursor = conn.cursor()
    print('Working on Password_dB.db')
    main()
