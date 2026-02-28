import random as r
dataset=list(range(1,100))
train=r.sample(dataset,70)
test=list(set(dataset)-set(train))
print(len(train),len(test))
