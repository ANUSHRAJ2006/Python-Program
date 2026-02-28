import numpy as np
'''create array with range'''
n6=np.arange(9)
print('n6',n6)
n7=np.arange(-5,30,5)
print('n7',n7)
'''linearly spaced entries'''
n8=np.linspace(0,20,num=8)
print('n8',n8)
n9=np.full([2,5],99)
print('n9',n9)
n9a=np.empty([1,3])
n9a.fill(9)
print('n9a',n9a)
