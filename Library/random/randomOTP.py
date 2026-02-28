import random as r
x=r.randint(1000,9999)
print(x)
user=int(input('Enter the OTP:'))
if user==x:
    print('Authentication is sucessfull')
else:
    print('Failed')
