import numpy as np
#boolean masking and advanced indexing


filedata =np.genfromtxt("data.txt", delimiter=',')
print(filedata)

filedata = filedata.astype('int32')

print(filedata)

print(filedata[filedata > 50])