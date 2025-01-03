import numpy as np
t2dml = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
t3dml = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])




'''
# get a specific ellement
# get a specific row
# get a specific column
# get a little more fancy - step period output numbers
# change value of some item
# change column items
# change row items
'''


# get a specific ellement
print(t2dml[1,5])
print(t2dml[0,6])
print(t2dml[1,1])

print(t3dml[0,1,1])

#get a specific row
print(t2dml[0,:])
print(t2dml[1,:])

#get a specific column
print(t2dml[:,0])
print(t2dml[:,3])
print(t2dml[:,6])

# step period output numbers
print(t2dml[0,0:7:1])
print(t2dml[1,1:6:2])

# change value of items
t2dml[1,5] = 20
t2dml[0,6] = 0
t2dml[1,1] = 34

t3dml[:,1,:] = [[9,9],[8,8]]

#change column items
t2dml[:,1] = 5
t2dml[:,4] = 20
t2dml[:,5] = 15

#change row items
t2dml[0,:] = 5
t2dml[1,:] = 20