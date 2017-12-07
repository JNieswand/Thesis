import numpy as np
import os
import glob
import io
import re
import copy
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import pyplot
from matplotlib import gridspec
# array of axies
gs = matplotlib.gridspec.GridSpec(1, 1)  #2 rows, 3 collums
# use this even for just 1 plot
# i.e. gs = gridspec.GridSpec(1, 1)
# so that the same methods are available

fig = pyplot.figure()

ax1 = fig.add_subplot(gs[0, 0])
#cbar_ax = fig.add_subplot(gs[:, 2])  # this axies streaches over all rows

# ax1.plot(....)


path = 'C:/Users/jnieswand/Desktop/Data_master/Speedtest/speeds.txt'


data =np.genfromtxt(path)
for i,dat in enumerate(np.transpose(data[1:])):
    if i ==0:
        res = copy.deepcopy(dat)
    else:
        ax1.plot(res,dat, linestyle = 'dashdot')
ax1.set_xlabel("Disparity resolution (refocussed pictures/disparity)")
ax1.set_ylabel("time in s")
labels = ["laplace","sobel", "depth", "depth_corr"]
ax1.legend(labels)
pyplot.savefig("C:/Users/jnieswand/Desktop/Python_master/Plots/speeds.png")
pyplot.close()  # releases the memeory