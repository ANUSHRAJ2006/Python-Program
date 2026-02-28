import re
text='The rain in spain fall mainly in plain'
patten=r'\b in \b'
matches=re.finditer(patten,text)
for match in matches:
    print('Match the word:', match.group())
