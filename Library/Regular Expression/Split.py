import re
text='I have 2 apples, 10 oranges and 5 bananas'
patten=r'\W'
split_text=re.split(patten,text)
print(split_text)
