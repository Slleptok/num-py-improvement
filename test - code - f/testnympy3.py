import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#iniitializing of different data types of arrays
#all 0s matrix

print(np.zeros((2,3,3,2)))

#all 1s matrix
print(np.ones((4,2,2)))

#any other numberss
print(np.full((2,2), 99, dtype="float32"))

#any other numberss(full-like)
print(np.full_like(a,4))

# decimal random number
print(np.random.random_sample(a.shape))

#random integer number
print(np.random.randint(4,7, size = (3,3)))

# the indentity matrix
print(np.identity(5))