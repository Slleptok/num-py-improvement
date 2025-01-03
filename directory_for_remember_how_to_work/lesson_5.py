import numpy as np




'''
# Use value from file
# Boolean masking and advanced indexing
'''

# use value from file
dataval =np.genfromtxt("data.txt", delimiter=',')
print(dataval)
dataval = dataval.astype('int32')
print(dataval)


#boolean masking and advanced indexing
filedata =np.genfromtxt("data.txt", delimiter=',')
print(filedata)
filedata = filedata.astype('int32')
print(filedata)
print(filedata[filedata > 50])