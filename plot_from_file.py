import numpy as np
import matplotlib.pyplot as plt


def open_file(file):
    f = file.read()
    inte = []
    hexa = []
    for i in range(len(f)):
        inte.append( f[i] )
    #    hexa.append( hex( f[i] ) )
    intearray = np.asarray(inte)
    
    windowSize = 1031 
    
    windowsNumbers = [intearray[x:x + 2] for x in range(2,len(intearray), windowSize) ]
    
    payload = [intearray[x:x + 1024] for x in range(5,len(intearray),windowSize) ]
    
    windowsNumbersCh0 = windowsNumbers[::512] 
    payloadCh0 = payload[::512]

    ch0 = zip(windowsNumbersCh0,payload)
    print(list(ch0))
    
    plt.figure()
    nPlots = 10
    for i in range(1,nPlots+1,1):
        plt.subplot(nPlots,1,i)
        plt.plot(payloadCh0[i][0:64][::2])
        plt.title('W# %s, Ch 0'% (i-1))
    plt.show()

file = open('data_vped1_25_amplifiershorted.bin','rb')
open_file(file)

