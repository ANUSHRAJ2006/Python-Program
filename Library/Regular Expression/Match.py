import re
patten=r'apples'
text='apples pie'
match=re.match(patten,text)
if match:
    print('Match Found!')
else:
    print('Not Found!')
