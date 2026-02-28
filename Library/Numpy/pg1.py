import numpy as np
'''1d array'''
n1=np.array([3,4,5,6])
print('n1',n1)
'''2d array'''
n2=np.array([[3,5,6,7],[4,5,6,7]])
print('n2',n2)
'''zero filled 2d array'''
n3=np.zeros([3,5])
print('n3',n3)
n3a=np.zeros([3,5],dtype='int32')
print('n3a',n3a)
'''array filled with ones'''
n4=np.ones([2,3,3],dtype='int32')
print('n4',n4)
'''empty array'''
n5=np.empty([1,3])
print('n5',n5)
'''Accessing'''
print('n1',n1[0])
print('n1',n1[-1])
print('n2',n2[1,0])
print('n2',n2[1,:])
print('n2',n2[:,3])
n4[1,1,2]=10
print('n4',n4)
'''size and shape'''
print('n4',n4.ndim)
print('n4',n4.shape)
print('n4',n4.size)
print('n4',n4.dtype)
print('n4',n4.itemsize)
print('n4',n4.nbytes)
