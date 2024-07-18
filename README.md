# Password Manager

This project is a password manager, deidacated to people like me, overwhelmed by accounts and passwords. It uses a simple database.db file where a table 'credentials' is created. It uses also the encrypt python library to encrypt the password variable and decrypt it only when called from the server, so as long as the password is in your database, no one can encrypt it without the token saved in yout token.txt file. Remember to have this specific file in your directory when you want to encrypt the database data.
You can also notice that I've created a specific function to check the python packages on your computer. If they are not, the program proceed to install them automatically with the command line, based on your operating system (also automatically checked).

## Prerequisites

Be aware of having Python 3.6 or a newest version installed, that's all!

## Installazione

1. Clona questa repository:
    ```bash
    git clone https://github.com/ZanelloG/PasswordManager.git
    cd PasswordManager
    ```

2. If the check_packagages function, for some reason, is not working, proceed with 2. and 3. :
    ```bash
    pip install cryptography
    ```

3. If you are using Linux and sqlite3 is not alredy installed:
    ```bash
    sudo apt-get install sqlite3
    ```

## How to use

1. Execute the script:
    ```bash
    python PasswordManager.py
    ```

2. Just follow the instruction printed in your shell to generate, load, add or show your credentials.

## File

- `PasswordManager.py`: Main script for the password manager.
- `token.txt`: File that contains the generated key.
- `Password_dB.dB` dB file where your credentials are stored (password encrypted)
