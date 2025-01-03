import numpy as np

before = np.array =[[1,2,3,4],[5,6,7,8]]

print(before)

# reshape by [4,2] or [8,1]
#after = before.reshape((8,1))
#print(after)


#verticaly stacking vectors
vb = np.array([1,2,3,4])
va = np.array([5,6,7,8])

print(np.vstack((vb,va,va,va)))


# horizontal stacking vectors

vb = np.zeros([2,4])
va = np.ones([2,2])
print(np.hstack((vb , va)))