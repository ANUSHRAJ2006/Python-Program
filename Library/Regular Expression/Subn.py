import re
patten=r'apples'
text='I have apples and apples or mangos'
new_text=re.subn(patten,'oranges',text)
print(new_text)
