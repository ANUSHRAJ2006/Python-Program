import numpy as np
'''indexing and slicing'''
n21=np.arange(10)
print('n21',n21)
print('n21',n21[n21<5])
print('n21',n21[(n21>3)&(n21<8)])
'''fiveup'''
fiveup=n21>5
print('fiveup',fiveup)
print(n21[fiveup])
'''nonzero'''
n21[6]=100
print('np.nonzero',np.nonzero(n21>5))
print('n21',n21[3:7])

'''stack and split'''
n22=np.array([[1,2],[3,4]])
n23=np.array([[5,6],[7,8]])
print('horizontal',np.hstack((n22,n23)))
print('vertical',np.vstack((n22,n23)))

n24=np.arange(20)
print('n24',n24)
print(np.hsplit(n24,4))

''''deep copy'''
n26=n24.copy()
n24[1]=200
print('n24',n24)
print('n26',n26)
