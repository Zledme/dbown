import sys
import json
import os
import requests
import argparse

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



#login
def login():
    user = input("Name: ")
    passw = input("Password: ")
    for line in open("user.txt","r").readlines():
        usr = line.split()
        if usr[0] == user:
            print('user found')    

#create new user
def create():
    print('Create')
    name = input('Name:')
    passw = input('Password:')
    with open('users.txt', 'w') as f:
        f.write(name+' '+hashed_password+'\n')

#update the user
def update():
    print('Update the password')
    passw1 = input('Enter New Password:')
    passw2 = input('Re-enter New Password:')
    with open('users.txt', 'w') as f:
        f.write('Logged in')

#delete a user
def delete():
    name = input('Enter the User to delete:')

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
    for line in open("user.txt","r").readlines():
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