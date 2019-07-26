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
import sys

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
            print("File decrypted.")
        except:
            print("Invalid input (Wrong password or File corrupted).")
            _main_()
    
def encrypt():
    bufferSize = 64*1024
    ok = 0
    while ok == 0:
        try:
            password = str(input("Encrypting file...\nEnter new main password (!!!DON'T FORGET IT!!!): "))
            if "'" in password or "\"" in password:
                print("Please don't use ' or \". Try again.")
            else:    
                password2 = str(input("Enter new main password again: "))
                if password == password2:
                    pyAesCrypt.encryptFile("password_list.txt", "password_list.txt.aes", password, bufferSize) 
                    ok += 1
                    print("File encrypted.")
                else:
                    print("Passwords don't match. Try again.")
        except:
            print("Invalid input (Wrong password or File corrupted).")
            encrypt()

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
            try:
                password_dict = ast.literal_eval("{"+password_dict+"}")
            except:
                password_dict = {}
    return password_dict

def create_new_password(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            if identifier in password_dict:
                print("Identifier already in use. Please add a new identifier or edit a previous one.")
                encrypt()
                _main_()
            else:
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

def manual_password(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier (unique value): "))
            if identifier in password_dict:
                print("Identifier already in use. Please add a new identifier or edit a previous one.")
                encrypt()
                _main_()
            else:
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
            password = str(input("Enter password manually: "))
            ok += 1
        except:
            print("Invalid input.")
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
            identifier = str(input("Identifier of what you want to edit: "))
            website = password_dict[identifier][0]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
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
    old_account = [website, login, old_password]
    account = [website, login, password]
    old_pass_line = {identifier : old_account}
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(str(old_pass_line)[1:len(str(old_pass_line))-1], str(pass_line)[1:len(str(pass_line))-1])
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def edit_manual_password(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier of what you want to edit: "))
            website = password_dict[identifier][0]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
    login = password_dict[identifier][1]
    old_password = password_dict[identifier][2]
    ok = 0
    while ok == 0:
        try:
            password = str(input("Enter password manually: "))
            ok += 1
        except:
            print("Invalid input.")
    password_dict[identifier][2] = password
    old_account = [website, login, old_password]
    account = [website, login, password]
    old_pass_line = {identifier : old_account}
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(str(old_pass_line)[1:len(str(old_pass_line))-1], str(pass_line)[1:len(str(pass_line))-1])
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def edit_nickname(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier of what you want to edit: "))
            website = password_dict[identifier][0]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
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
    old_account = [website, old_login, password]
    account = [website, login, password]
    old_pass_line = {identifier : old_account}
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(str(old_pass_line)[1:len(str(old_pass_line))-1], str(pass_line)[1:len(str(pass_line))-1])
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def edit_website(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier of what you want to edit: "))
            old_website = password_dict[identifier][0]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
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
    old_account = [old_website, login, password]
    account = [website, login, password]
    old_pass_line = {identifier : old_account}
    pass_line = {identifier : account}
    with open('password_list.txt', 'r') as f :
        filedata = f.read()
        filedata = filedata.replace(str(old_pass_line)[1:len(str(old_pass_line))-1], str(pass_line)[1:len(str(pass_line))-1])
    with open('password_list.txt', 'w') as f:
        f.write(filedata)    
    f.close()
    return [pass_line, identifier]

def delete_line(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier of what you want to delete: "))
            del password_dict[identifier]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
    with open('password_list.txt', 'w') as f:
        f.write(str(password_dict)[1:len(str(password_dict))-1])
    f.close()

def search_line(password_dict):
    ok = 0
    while ok == 0:
        try:
            identifier = str(input("Identifier of what you want to search: "))
            password_line = password_dict[identifier]
            ok += 1
        except:
            print("Entry not found.")
            encrypt()
            _main_()
    return password_line

def _main_():
    ok = 0
    while ok == 0:
        try:
            command = str(input("What do you want to do?\n(A)dd an entry\n(E)dit an entry\n(D)elete an entry\n(S)earch an entry\n(V)iew all entries\n(Q)uit\n\nEnter command: "))
            if command.lower() in "aedsvq":
                ok += 1
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    if command.lower() == "a":
        password_dict = get_password_collection()
        ok = 0
        while ok == 0:
            try:
                manual = input("Enter password manually? (y/n): ")
                if manual.lower() == "y" or manual.lower() == "n":
                    ok += 1
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
        if manual.lower() == "n":
            new_password_list = create_new_password(password_dict)
            new_password = new_password_list[0]
            identifier = new_password_list[1]
            password_dict.update(new_password)
            print("Entry created!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_password[identifier][0]+"\nNickname or email address: "+new_password[identifier][1]+"\nPassword: "+new_password[identifier][2])
        elif manual.lower() == "y":
            new_password_list = manual_password(password_dict)
            new_password = new_password_list[0]
            identifier = new_password_list[1]
            password_dict.update(new_password)
            print("Entry created!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_password[identifier][0]+"\nNickname or email address: "+new_password[identifier][1]+"\nPassword: "+new_password[identifier][2])
    elif command.lower() == "e":
        if not os.path.isfile("password_list.txt.aes"):
            print("*No entry to edit.*")
            _main_()
        else:
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
                ok = 0
                while ok == 0:
                    try:
                        manual = input("Enter password manually? (y/n): ")
                        if manual.lower() == "y" or manual.lower() == "n":
                            ok += 1
                        else:
                            print("Invalid input.")
                    except:
                        print("Invalid input.")
                if manual.lower() == "n":
                    edit_password_list = edit_password(password_dict)
                    new_password = edit_password_list[0]
                    identifier = edit_password_list[1]
                    password_dict.update(new_password)
                    print("Password edited!\nIdentifier (unique value): "+identifier+"\nWebsite name or url: "+new_password[identifier][0]+"\nNickname or email address: "+new_password[identifier][1]+"\nPassword: "+new_password[identifier][2])
                elif manual.lower() == "y":
                    edit_password_list = edit_manual_password(password_dict)
                    new_password = edit_password_list[0]
                    identifier = edit_password_list[1]
                    password_dict.update(new_password)
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
        if not os.path.isfile("password_list.txt.aes"):
            print("*No entry to delete.*")
            _main_()
        else:
            password_dict = get_password_collection()
            delete_line(password_dict)
            print("Entry deleted!")
    elif command.lower() == "s":
        if not os.path.isfile("password_list.txt.aes"):
            print("*No entry to search.*")
            _main_()
        else:
            password_dict = get_password_collection()
            password_line = search_line(password_dict)
            print("Website name or url: "+password_line[0]+"\nNickname or email address: "+password_line[1]+"\nPassword: "+password_line[2])
    elif command.lower() == "v":
        if not os.path.isfile("password_list.txt.aes"):
            print("*No entry to show.*")
            _main_()
        else:
            password_dict = get_password_collection()
            print("\n'Identifier': ['Website', 'Nickname / Email', 'Password']\n")
            if len(password_dict) == 0:
                print("*No entry to show.*")
            else:
                print(str(str(password_dict)[1:len(str(password_dict).replace("], ", "]\n"))-1].replace("], ", "]\n")+"]\n\n"))
    elif command.lower() == "q":
        raise sys.exit()
    else:
        print("Invalid input.")
        _main_()
    encrypt()
    os.remove("password_list.txt")
    print("password_list.txt moved to Trash / Recycling bin.\nDelete it and close this window for full protection.")
        
_main_()
