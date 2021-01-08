import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Tkagg')
import itertools
import matplotlib.gridspec as gridspec
from pylab import *
import matplotlib.animation as animation
import pandas as pd
import os
import pickle
"""
Create a column per channel from list
"""
# Creating fake data
payloadSize= 5
num_channels= 4
ser_data=[]
for i in range(0, num_channels):
    for j in range(0,payloadSize):
        ser_data.append(i)

payload=[]
incoming_data=[]
incoming_data = [33]+[1]+ser_data+[33]
print(incoming_data)

# Extracting values
wdoNumber= incoming_data[1]
payload = incoming_data[2:2 + payloadSize*num_channels]
print (payload)

payload_arr = np.array([np.array(xi) for xi in payload])

print (payload_arr)

payload_arr_rsh = payload_arr.reshape(num_channels,payloadSize)

print(payload_arr_rsh.transpose())

filetosave = 'test.csv'
np.savetxt(filetosave, payload_arr_rsh.transpose(), delimiter=',')

# if file does not exist write header 
if not os.path.isfile(filetosave):
    np.savetxt(filetosave,payload_arr_rsh, 'ab',fmt='%1.3f')
else: # else it exists so append without writing the header
    f=open(filetosave, 'ab')
    f.write(payload_arr_rsh)
    f.close()
#pickle.dump( payload_arr_rsh.transpose(), open( "save.p", "wb" ) )
