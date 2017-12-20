# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import io
import glob
import os
import numpy as np
import re
import matplotlib
from matplotlib import pyplot
from matplotlib import gridspec
# array of axies
gs = matplotlib.gridspec.GridSpec(1, 1)  #2 rows, 3 collums
# use this even for just 1 plot
# i.e. gs = gridspec.GridSpec(1, 1)
# so that the same methods are available

fig = pyplot.figure()

ax = fig.add_subplot(gs[0, 0])

resolution = 1
path = 'C:/Users/jnieswand/Documents/Thesis/Data_master/Ground_truth_analysis/complex_res'+str(resolution)+'/'
files = glob.glob( os.path.join(path, '*erroranalysis*') )
meansqu = np.array([])
for file in files:
            s = 'standard deviation';
            with io.open(file, 'r') as f:
                for line in f:
                    if 'mean squared error' in line:
                        x = np.float(re.findall('[\\d.]+', line)[0])
                        meansqu = np.append(meansqu, x)
                        
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

tup = tuple(['corr', 'cropped', 'depth', 'cropped', 'laplace', 'cropped', 'sobel', 'cropped'])    
i = np.arange(len(files))

ax.bar(i, meansqu)
plt.xticks(i, tup , rotation = 30)
ax.set_ylabel('mean squared error')
pyplot.savefig('C:/Users/jnieswand/Documents/Thesis/Python_master/Plots/error_res'+str(resolution))
pyplot.close()