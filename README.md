# dbown

# dependencies
1. python3
also install requests library:
```bash
 pip install requests
```

# Login
User: Admin
Password: NewPassword

# Usage
```bash
cd dbown

#for login , use the user and password given at first
python main.py --login
#you can only use other command if the user is logged in


#for getting data with longitude and latitude
python main.py --getbyll 52 22

#for getting data with city name
python main.py --getbycn nanital
```
## command to use
-h, --help         : show this help message and exit

--login          : to login

--logout         :  to logout

--create         : create new user

--update         : update user

--delete         : delete user

--showall        :  show all users

--getbyll lon lat:  get the data through longitude and latitude

--getbycn city   :  get the data through cityname
