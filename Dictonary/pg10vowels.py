x='The design and implementation of a Voice Recognition-Based Automated Trading System using Python, Natural Language Processing (NLP)'
vow='aeiou'
x=x.lower()
x1={}
for i in vow:
    x1[i]=0
print(x1)
for i in x:
    if i in x1.keys():
        x1[i]+=1
print(x1)
