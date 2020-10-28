import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Tkagg')
import itertools
import matplotlib.gridspec as gridspec
#from pylab import *
#import matplotlib.animation as animation
import pandas as pd

"""
Create a column per channel from list
"""
# Creating fake data
payloadSize= 512
num_channels= 16
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
# Creating list of column names
list_ch = ['ch0', 'ch1', 'ch2','ch3','ch4','ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10',' ch11', 'ch12', 'ch13', 'ch14', 'ch15']
# List of list from data
list_of_list = [ payload[x: x + payloadSize] for x in range(0,num_channels*payloadSize,payloadSize)]
# Dataframe
dfnew = pd.DataFrame.from_records(list_of_list)
dfnew = dfnew.transpose()
print(dfnew)
dfnew.columns= list_ch

# if file does not exist write header 
if not os.path.isfile('filename.csv'):
   dfnew.to_csv('filename.csv', header='column_names', sep='\t')
else: # else it exists so append without writing the header
   dfnew.to_csv('filename.csv', mode='a', header=False, sep=' ')
#file_name = 'output.csv'
#dfnew.to_csv(file_name,mode= 'a' ,sep='\t')
print(dfnew)





