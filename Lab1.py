"""
CS2302
Lab 1 Part B
Purpose: Implement a recursive method to generate all possible passwords (brute force)
Created on September 9, 2019
Diego Aguirre
@author: Nancy Hernandez
"""
import hashlib
import time


# Provided code
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


# Creates passwords
def generate(password, min_length):
    # Minimum of length 3
    if len(password) == min_length:
        test(password)
        return

    # Will go from 0 to 9 only
    for i in range(10):
        generate(password + str(i), min_length)


# Reads file and compares hashed values to determine correct password
def test(password):
    count = 0
    password_file = open("password_file.txt", "r")

    # Reads file
    for line in password_file:
        password_list = line.split(",")

        # Determines what each item in line is
        username = password_list[0]
        salt = password_list[1].replace("\n", "")
        hashed_value = password_list[2].replace("\n", "")

        # Hashes generated password with salt value
        new_hashed = hash_with_sha256(password + salt)

        if new_hashed == hashed_value:
            print(username, 'password is:', password)

    password_file.close()

def main():
    # Will begin as empty rather than at 0
    password = ""

    start = time.time()

    # Password minimum and maximum lengths
    for i in range(3, 8):
        generate(password, i)
    print('Done')

    end = time.time()
    print(end - start, 'seconds')

main()
