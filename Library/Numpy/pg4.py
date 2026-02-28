import numpy as np
'''converting 1d to 2d'''
n16=np.arange(8)
print('n16',n16)
n17=n16[np.newaxis,:]
print('n17',n17)
print(n17.shape)
n18=n16[:,np.newaxis]
print('n18',n18)
print(n18.shape)
