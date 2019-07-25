#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:56:29 2019

@author: DaveTremblay
"""

import random
import os
import ast
import pyAesCrypt

def random_password(length, strength):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = uppercase.lower()
    numerical = "0123456789"
    symbology = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    
    char_type = {
            1 : uppercase,
            2 : lowercase,
            3 : numerical,
            4 : symbology
            }
    
    password = ""
    
    for n in range(length):
        x = random.randint(1,strength)
        y = random.randint(1,len(char_type[x])-1)
        character = char_type[x][y]
        password += character

    return password

def decrypt():
    bufferSize = 64*1024
    ok = 0
    while ok == 0:
        try:
            password = str(input("Decrypting file...\nEnter main password to access encrypted passwords: "))
            pyAesCrypt.decryptFile("password_list.txt.aes", "password_list.txt", password, bufferSize) 
            ok += 1
        except:
            print("Invalid input (Wrong password or File corrupted).")
    
def encrypt():
    bufferSize = 64*1024
    ok = 0
    while ok == 0:
        try:
            password = str(input("Encrypting file...\nEnter new main password (!!!DON'T FORGET IT!!!): "))
            pyAesCrypt.encryptFile("password_list.txt", "password_list.txt.aes", password, bufferSize) 
            ok += 1
        except:
            print("Invalid input (Wrong password or File corrupted).")

def get_password_collection():
    if not os.path.isfile("password_list.txt") and not os.path.isfile("password_list.txt.aes"):
        password_dict = {}
        with open("password_list.txt", "w") as f:
            f.close()
    else:
        decrypt()
        os.remove("password_list.txt.aes")
        with open("password_list.txt", "r") as f:
            password_dict = f.read()
            password_dict = ast.literal_eval("{"+password_dict+"}")
    return password_dict

def create_new_password():
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            ok += 1
        except:
            print("Invalid input.")
    ok = 0
    while ok == 0:
        try:
            website = str(input("Website name or url: "))
            ok += 1
        except:
            print("Invalid input.")
    ok = 0
    while ok == 0:
        try:
            login = str(input("Nickname / Email address: "))
            ok += 1
        except:
            print("Invalid input.")
    ok = 0
    while ok == 0:
        try:
            length = int(input("Desired password length: "))
            if length > 0:
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    ok = 0
    while ok == 0:
        try:
            strength = int(input("Strength\n1: Uppercase\n2: 1 + lowercase\n3: 2 + numbers\n4: 3 + special characters\n\nDesired password strength (1-4): "))
            if strength > 0 and strength < 5:
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    password = random_password(length, strength)
    account = [website, login, password]
    pass_line = {identifier : account}
    with open("password_list.txt", "a") as f:
        f.write(str(pass_line)[1:len(str(pass_line))-1] + ",\n")
    f.close()
    return [pass_line, identifier]

def edit_password(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            website = password_dict[identifier][0]
            ok += 1
        except:
            print("Invalid input.")
    login = password_dict[identifier][1]
    old_password = password_dict[identifier][2]
    ok = 0
    while ok == 0:
        try:
            length = int(input("Desired new password length: "))
            if length > 0:
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    ok = 0
    while ok == 0:
        try:
            strength = int(input("Strength\n1: Uppercase\n2: 1 + lowercase\n3: 2 + numbers\n4: 3 + special characters\n\nDesired new password strength (1-4): "))
            if strength > 0 and strength < 5:
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    password = random_password(length, strength)
    password_dict[identifier][2] = password
    account = [website, login, password]
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(old_password, password)
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def edit_nickname(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            website = password_dict[identifier][0]
            ok += 1
        except:
            print("Invalid input.")
    old_login = password_dict[identifier][1]
    password = password_dict[identifier][2]
    ok = 0
    while ok == 0:
        try:
            login = str(input("New account name / email address: "))
            ok += 1
        except:
            print("Invalid input.")
    password_dict[identifier][1] = login
    account = [website, login, password]
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(old_login, login)
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def edit_website(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            old_website = password_dict[identifier][0]
            ok += 1
        except:
            print("Invalid input.")
    login = password_dict[identifier][1]
    password = password_dict[identifier][2]
    ok = 0
    while ok == 0:
        try:
            website = str(input("New website name or url: "))
            ok += 1
        except:
            print("Invalid input.")
    password_dict[identifier][0] = website
    account = [website, login, password]
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(old_website, website)
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def delete_line(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            del password_dict[identifier]
            ok += 1
        except:
            print("Invalid input.")
    with open('password_list.txt', 'w') as f:
        f.write(str(password_dict)[1:len(str(password_dict))-1] + ",\n")
    f.close()

def search_line(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            password_line = password_dict[identifier]
            ok += 1
        except:
            print("Invalid input.")
    return password_line

def _main_():
    ok = 0
    while ok == 0:
        try:
            command = str(input("What do you want to do?\n(A)dd an entry\n(E)dit an entry\n(D)elete an entry\n(S)earch an entry\n(V)iew all entries\n\nEnter command: "))
            if command.lower() in "aedsv":
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    if command.lower() == "a":
        password_dict = get_password_collection()
        new_password_list = create_new_password()
        new_password = new_password_list[0]
        identifier = new_password_list[1]
        password_dict.update(new_password)
        print("Entry created!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_password[identifier][0]+"\nNickname or email address: "+new_password[identifier][1]+"\nPassword: "+new_password[identifier][2])
    elif command.lower() == "e":
        ok = 0
        while ok == 0:
            try:
                command_2 = str(input("What do you want to edit?\n(W)ebsite name or url\n(N)ickname or Email address\n(P)assword\n\nEdit: "))
                if command_2.lower() in "wnp":
                    ok += 1
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
        if command_2.lower() == "p":
            password_dict = get_password_collection()
            edit_password_list = edit_password(password_dict)
            new_password = edit_password_list[0]
            identifier = edit_password_list[1]
            print("Password edited!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_password[identifier][0]+"\nNickname or email address: "+new_password[identifier][1]+"\nPassword: "+new_password[identifier][2])
        elif command_2.lower() == "n":
            password_dict = get_password_collection()
            edit_nickname_list = edit_nickname(password_dict)
            new_nickname = edit_nickname_list[0]
            identifier = edit_nickname_list[1]
            print("Nickname or email address edited!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_nickname[identifier][0]+"\nNickname or email address: "+new_nickname[identifier][1]+"\nPassword: "+new_nickname[identifier][2])
        elif command_2.lower() == "w":
            password_dict = get_password_collection()
            edit_website_list = edit_website(password_dict)
            new_website = edit_website_list[0]
            identifier = edit_website_list[1]
            print("Website name or url edited!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_website[identifier][0]+"\nNickname or email address: "+new_website[identifier][1]+"\nPassword: "+new_website[identifier][2])
    elif command.lower() == "d":
        password_dict = get_password_collection()
        delete_line(password_dict)
        print("Entry deleted!")
    elif command.lower() == "s":
        password_dict = get_password_collection()
        password_line = search_line(password_dict)
        print("Website name or url: "+password_line[0]+"\nNickname or email address: "+password_line[1]+"\nPassword: "+password_line[2])
    elif command.lower() == "v":
        password_dict = get_password_collection()
        print("\n'Identifier': ['Website', 'Nickname', 'Password']\n")
        print(str(password_dict)[1:len(str(password_dict).replace("], ", "]\n"))-1].replace("], ", "]\n")+"]")
    encrypt()
    os.remove("password_list.txt")
    print("password_list.txt moved to Trash / Recycling bin.\nDelete it and close this window for full protection.")
        
_main_()
