import re
patten=r'\d+'
text='There are 100 apples and 200 oranges'
matches=re.findall(patten,text)
if matches:
    print('Found:',matches)
else:
    print('Not Found')
