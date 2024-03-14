# Programmer: Lauryn Meyer
# Date: 3-12-2024
# Program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA


import hashlib
import getpass

def hash_password(password, salt):
    # Concatenate password and salt, then hash
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def main():
    password = getpass.getpass("Enter your password: ")
    salt = "somesalt"  # You can generate a random salt if you want
    hashed_password = hash_password(password, salt)
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
