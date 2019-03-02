import numpy as np
import matplotlib.pyplot as plt
import itertools
"""
Function for get windows and payload from
a file and plot the results 
"""

def open_file(file):
    intearray = np.fromfile(file, dtype = np.uint16)
    windowSize = 1030 
    
    windowsNumbers = [intearray[x] for x in range(1,len(intearray), int(windowSize/2)) ]
    
    payload = [intearray[x:x + 512] for x in range( 2,len(intearray), int(windowSize/2) ) ]
    
     
    print('len payload',len(payload))
    
    
    windows_and_channels = [ [ payload[i][ x:x + 32] for x in range(16)   ] for i in range(15)]
    


    print(len(windows_and_channels[0]))
    print(len(windows_and_channels[0][0]))
    print(len(windows_and_channels[0][0]))
    print(windows_and_channels[0][13])
    
    ch0_all_windows = list()
    
    def same_channel(channel, numberWindows):
        sameChannel=list()
        for i in range(numberWindows):
            sameChannel += windows_and_channels[i][channel].tolist()
        return sameChannel
    
    plt.figure()
    nPlots = 15
    for i in range(1,nPlots+1,1):
        plt.subplot(nPlots,1,i)
        plt.plot(same_channel(i,15))
        plt.title('W# %s, Ch 0'% (i-1))
    plt.show()


#for i in range(100):
#file = open('data_vped1_25_amplifiershorted.bin','rb')
file = open('15_windowsSineWave.bin','r')

open_file(file)
#input("Press Enter to continue...")


