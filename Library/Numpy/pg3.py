import numpy as np
'''sorting'''
n10=np.array([3,4,1,9,5,10,8,7])
print('n10',np.sort(n10))
n11=np.array([[6,2,7],[5,10,1]])
print('n11',np.sort(n11,axis=1))
print('n11',np.sort(n11,axis=0))
'''resaping and array conversion'''
n12=n10.reshape(2,4)
print('n12',n12)
'''join 2 array using concatenate'''
n13=np.arange(4)
print('n13',n13)
n14=np.arange(5,9)
print('n14',n14)
n15=np.concatenate((n13,n14))
print('n15',n15)
