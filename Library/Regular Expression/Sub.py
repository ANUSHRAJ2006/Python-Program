import re
patten=r'apples'
text='I have apples and apples'
new_text=re.sub(patten,'oranges',text)
print(new_text)
