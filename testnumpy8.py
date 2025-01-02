import numpy as np

dataval =np.genfromtxt("data.txt", delimiter=',')
print(dataval)

dataval = dataval.astype('int32')

print(dataval)