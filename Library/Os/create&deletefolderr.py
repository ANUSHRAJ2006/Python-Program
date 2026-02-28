import os
if not os.path.exists('Test folder'):
    os.mkdir('Test folder')
    print('Folder Created')
else:
    print('Folder already exists')
os.rmdir('Test Folder')
print('Folder Deleted')
