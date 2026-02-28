db={'test':'0001'}
def signup():
    username=input('Enter the New Username:')
    password=input('Enter the New Password:')
    if username in db.keys():
        print('Account already exist try new username or try again')
        user()
    else:
        db[username]=password
        print('Account created successfully')
        login()
def login():
    username=input('Enter the  Username:')
    password=input('Enter the  Password:')
    if username in db.keys() and db[username]==password:
        print('Login Sucessfully')
    else:
        print('usrname or password invalid')
        login()
def user():
    user=input('if you have an existing account choose "y" else press any key').lower()
    if user=="y":
        login()
    else:
        signup()
    
