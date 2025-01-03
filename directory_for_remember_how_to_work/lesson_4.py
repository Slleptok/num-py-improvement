import numpy as np




'''
# copy arrays
# mathematics (+-/*)
# min & max of arrays value
# reshaping
# vertivaly stacking vectors
# horizontal stacking vectors
'''


# copy arrays
t1dml1 = np.array([1,2,3])
t1dml2 = t1dml1.copy()

# mathematics
# +
t1dml3 = np.array([1,2,3,4])
print(t1dml3 + 3)
# -
t1dml3 = np.array([1,2,3,4])
print(t1dml3 - 3)
# /
t1dml3 = np.array([1,2,3,4])
print(t1dml3 / 3)
# *
t1dml3 = np.array([1,2,3,4])
print(t1dml3 * 3)


# min & max of arrays value
t1dml4 = np.array([[1,2,3],[4,5,6]])
print(np.min(t1dml4))
print(np.max(t1dml4))


#reshaping
before = np.array =[[1,2,3,4],[5,6,7,8]]
print(before)
# reshape by [4,2] or [8,1]
after = before.reshape((8,1))
print(after)


#verticaly stacking vectors
vb = np.array([1,2,3,4])
va = np.array([5,6,7,8])
print(np.vstack((vb,va,va,va)))


# horizontal stacking vectors
vb = np.zeros([2,4])
va = np.ones([2,2])
print(np.hstack((vb , va)))


