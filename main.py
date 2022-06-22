import sys
import json
import os
import requests
import argparse
import hashlib, binascii

BASE_URL = 'https://api.openweathermap.org/data/2.5/'
KEY = '34f4a8299883147d27107370411a142c'


parser = argparse.ArgumentParser(description='nothing for now')
parser.add_argument('--login',action='store_true', help='to login')
parser.add_argument('--logout',action='store_true', help='to logout')
parser.add_argument('--create',action='store_true', help='create new user')
parser.add_argument('--update',action='store_true', help='update user')
parser.add_argument('--delete',action='store_true', help='delete user')
parser.add_argument('--showall',action='store_true', help='show all users')
parser.add_argument('--getbyll',nargs=2,metavar=('lon','lat'),help='get the data through longitude and latitude')
parser.add_argument('--getbycn',nargs=1,metavar='city',help='get the data through cityname')

args = parser.parse_args()


#hashing password
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),
    salt,100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt+password_hash).decode('ascii')

def check_password(stored_password, user_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512',user_password.encode('utf-8'),
    salt.encode('ascii'),
    100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password



#login
def login():
    user = input("User: ")
    passw = input("Password: ")
    for line in open("users.txt","r").readlines():
        usr = line.split()
        if usr[0] == user:
            return check_password(usr[1], passw)
    return False

#create new user
def create():
    print('Create')
    name = input('Name:')
    passw = input('Password:')
    with open('users.txt', 'w') as f:
        f.write(name+' '+hash_password(passw)+'\n')

#update the user
def update():
    print('Update the password')
    user = input('Enter the user:')
    passw1 = input('Enter New Password:')
    checkexist = False
    with open('users.txt', 'r') as f:
        lines = f.readlines()

        with open('users.txt','w') as fw:
            for line in lines:
                usr = line.split()
                if usr[0] != user:
                    fw.write(line)
                if usr[0] == user:
                    checkexist = True
                    fw.write(user+' '+hash_password(passw1)+'\n')
             
    if not checkexist:
        print("user doesn't exist")
#delete a user
def delete():
    name = input('Enter the User to delete:')
    checkexist = False
    with open('users.txt', 'r') as f:
        lines = fr.readlines()

        with open('months.txt','w') as fw:
            for line in lines:
                usr = line.split()
                if usr[0] != user:
                    fw.write(line)
                if usr[0] == user:
                    checkexist = True
    if not checkexist:
        print("user doesn't exist")
#getdata
def getdata(query_params):
    response = requests.get(f'{BASE_URL}/weather',params=query_params)
    #print(response.json())
    data = response.json()
    
    print('1. Humidity:',data['main']['humidity'])
    print('2. Pressure:',data['main']['pressure'])
    print('3. Average Temperature:',data['main']['temp'])
    print('4. Wind Speed:',data['wind']['speed'])
    print('5. Wind degree:',data['wind']['deg'])
    print('6. UV index:')


#call the api
def show_all():
    for line in open("users.txt","r").readlines():
        usr = line.split()
        print(usr[0])


#check if the user is logged in or not
def checklogin():
    return os.path.exists('login.txt')


#logout user
def main():
    if args.login:
        if checklogin():
            print('you are logged in already')
        else:
            chances = 3
            while chances > 0:
                if login():
                    with open('login.txt', 'w') as f:
                        f.write('Logged in')
                    exit()
                chances -=1
            print('Retry the command')


    if args.create:
        if checklogin():
            create()
        else:
            print('not logged in')
    if args.update:
        if checklogin():
            update()
        else:
            print('not logged in')
    if args.delete:
        if checklogin():
            delete()
        else:
            print('not logged in')
    if args.showall:
        if checklogin():
            show_all()
        else:
            print('not logged in')

    if '--getbyll' in sys.argv:
        if checklogin():
            query_params = {
                "lat":args.getbyll[0],
                "lon":args.getbyll[1],
                "appid":KEY
            }
            getdata(query_params)            
        else:
            print('not logged in') 
    
    
    if '--getbycn' in sys.argv:
        if checklogin():
            if checklogin():
                query_params = {
                "q":args.getbycn[0],
                "appid":KEY
            }
            getdata(query_params)
        else:
            print('not logged in')

    if args.logout:
        if checklogin():
            os.remove("login.txt") 
        else:
            print('not logged in')
            
if __name__ == '__main__':
    main()