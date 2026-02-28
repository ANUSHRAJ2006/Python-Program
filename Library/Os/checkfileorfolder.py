import os
name='Date'
if os.path.isfile(name):
    print(name,'is a file')
elif os.path.isdir(name):
    print(name,'is a folder')
else:
    print("Not found")
