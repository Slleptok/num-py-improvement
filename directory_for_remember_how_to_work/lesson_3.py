import numpy as np
t2dml = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])





#just initializing of different types of arrays
'''
# make a 0-s matrix
# make a 1-s matrix
# other numbers
# use full_like for numbers
# decimal random number
# integer random number
# the indentity matrix
'''

#make a 0-s matrix
print(np.zeros((2,3,3,3)))

# make a 1-s matrix
print(np.ones((4,2,2)))

# full another number
print(np.full([2,2], 99, dtype='float32'))

# full another number using 'full_like'
# here ('array', 'number will be full')
print(np.full_like(t2dml, 4))

# decimal random number
print(np.random.random_sample(t2dml.shape))

# random integer number
# here ('low number','high number', size=(3,3))
print(np.random.randint(4,7, size=(3,3)))

# the identity matrix
print(np.identity(5))
print(np.identity(9))
print(np.identity(2))