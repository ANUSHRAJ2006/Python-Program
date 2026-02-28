import random as r
data=list(range(1,21))
r.shuffle(data)
train=data[:14]
test=data[14:]
print('Train',train)
print('Test',test)
