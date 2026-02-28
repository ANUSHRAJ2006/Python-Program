import re
patten=r'\d+'
text='There are 100,200 apples'
match=re.search(patten,text)
if match:
    print('Found:',match.group())
else:
    print('Not Found')
