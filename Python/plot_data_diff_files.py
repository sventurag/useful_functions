import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
plt.style.use('bigFontsize') # matplotlib style file


"""
Script to plot data from different files, 
it is used for the output of the oscilloscope in IDLAB
"""

# Getting the data from different files, creating a list of dataframes
cols=["Time","Trigger"]
df=list()
for i in range(81,132,1):
    fileName = ("".join("./trigger/"+"trigger"+str(i)+".csv"))
    df.append( pd.read_csv ( fileName, sep=",",names=cols, header=None,skiprows=21 ))

#Plotting the list of dataframes
ax=plt.gca()
maxList =list()
for i in range(0,40,1):
    maximus = df[i]['Trigger'].max() 
    if maximus  >= 0.025:
        df[i].plot(x='Time', y='Trigger',legend=False, marker= 'o', markersize=1, markerfacecolor='black', markeredgecolor='black', ax=ax)
        maxList.append(df[i].loc[df[i]['Trigger'].idxmax() ].Time )# Maximum value of the trigger in the time column

        plt.ylabel('Amplitude [V]')
        plt.xlabel('Time [s]')

plt.figure()
plt.plot(maxList, marker= 'o', markersize=1, markerfacecolor='black', markeredgecolor='black')
plt.ylabel('PulseMax Time[s]')
plt.xlabel('Pulse number')

#Plotting the position in time of the maximum value of the pulses
plt.figure()
plt.hist(maxList, 10)
plt.ylabel('Time[s]')
plt.xlabel('Pulses')
print(np.std(maxList)/1e-9)


# Histogram and fit plotted

data=maxList

# Fit a normal distribution to the data:
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
print(xmin,xmax)
x = np.linspace(xmin, xmax,5)
print(x)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = {:.2E},  std = {:.2E}".format (mu, std)
plt.title(title)

plt.show()


