import sys
import json
import os

import argparse

parser = argparse.ArgumentParser(description='nothing for now')
parser.add_argument('--login',action='store_true', help='to login')
parser.add_argument('--logout',action='store_true', help='to logout')
parser.add_argument('--create',action='store_true', help='create new user')
parser.add_argument('--update',action='store_true', help='update user')
parser.add_argument('--delete',action='store_true', help='delete user')
parser.add_argument('--showall',action='store_true', help='show all users')
args = parser.parse_args()



#login
def login():
    users = show_all()
    user = input("Name: ")
    passw = input("Password: ")

    if user in users.keys():
        if passw == users[user]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:
        print("Hello, new person.")
        users[user] = passw

    writeUsers(users)
    return True

#call the api
def show_all():
    with open("users.json","r") as f:
        return json.load(f)


#check if the user is logged in or not
def checklogin():
    return False


#logout user
def main():
    if args.login:
        if checklogin():
            print('you are logged in already')
        else:
            login()

            

            
    
    if args.create:
        if checklogin():
            print('Create')
            name = input('Name:')
            passw = input('Password:')
        else:
            print('not logged in')
    if args.update:
        if checklogin():
            print('Update the password')
            passw1 = input('Enter New Password:')
            passw2 = input('Re-enter New Password:')
        else:
            print('not logged in')
    if args.delete:
        if checklogin():
            name = input('Enter the User to delete:')
        else:
            print('not logged in')
    if args.showall:
        if checklogin():
            users = show_all()
        else:
            print('not logged in')

    if args.getdata:
        pass


    if args.logout:
        if checklogin():
            pass
        else:
            print('not logged in')
            
if __name__ == '__main__':
    main()