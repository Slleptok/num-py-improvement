import numpy as np




'''
# we made a 1 2 & 3 dimentionals lists
# using numpy
'''
# create a Numpy arrray
t1dml = np.array([1,2,3])
print(t1dml)

# create a 2 dimentional list
t2dml = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])

#create a 3 dimentional list
t3dml = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])




'''
# checking the numbers of dimentions
# cheking shape of lists
# get data type of values in list
# change data type of lists
'''
# checking the numbers of dimentions
print(t1dml.ndim)
print(t2dml.ndim)
print(t3dml.ndim)

# cheking shape of lists
print(t1dml.shape)
print(t2dml.shape)
print(t3dml.shape)


# get data type of values in list
print(t1dml.dtype)
print(t2dml.dtype)
print(t3dml.dtype)

# change data type of lists
changedtype1 = np.array([1,2,3], dtype='int16')
changedtype2 = np.array([1,2,3], dtype='int32')
changedtype3 = np.array([1,2,3], dtype='float32') # etc...




'''
# item size
# list size
# multiply var sizes
# number of bytes size
'''
#item size
print(t1dml.itemsize)
print(t2dml.itemsize)
print(t3dml.itemsize)

#list size
print(t1dml.size)
print(t2dml.size)
print(t3dml.size)

#multiplying
print(t1dml.itemsize * t1dml.size)
print(t2dml.itemsize * t2dml.size)

#number of bytes size
print(t1dml.nbytes)
print(t2dml.nbytes)
print(t3dml.nbytes)