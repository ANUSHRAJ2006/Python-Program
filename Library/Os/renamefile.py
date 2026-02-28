import os
cwd='cwd.py'
cwd1='cwd1.py'
if os.path.exists(cwd):
    os.rename(cwd,cwd1)
    print('Renamed')
else:
    print('File not Found')
