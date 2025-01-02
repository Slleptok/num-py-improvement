import numpy as np

a = np.array([1,2,3])

print(a)

b = np.array([[9.0,8.0,7.0,],[6.0,5.0,4.0]])

print(b)

#Diension
print(a.ndim)
print(b.ndim)

#shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

# change data type
c = np.array([1,2,3], dtype="int16")

# item size

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# total size

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# multiply var sizes
print(a.itemsize * a.size)

# get size number bytes
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)


