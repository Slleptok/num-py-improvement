import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)
print(a.shape)

#Get a specific ellement
print(a[1,5])

#get a specific row
print(a[0,:])

#get a pecific column
print(a[:,2])

#get a little more fancy [startindex,endindex,stepsize]
print(a[0,1:6:2])# output  = 2 4 6

#change value of some item
a[1,5] = 20
print(a)

#change column items
a[:,1] = 5
print(a)

#3d example

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#get specific element (work outside in)
print(b[0,1,1])

#replace
b[:,1,:] = [[9,9],[8,8]]
print(b)


