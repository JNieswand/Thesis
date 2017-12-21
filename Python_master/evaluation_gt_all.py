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
import matplotlib.patches as mpatches
# array of axies
gs = matplotlib.gridspec.GridSpec(1, 1)  #2 rows, 3 collums
# use this even for just 1 plot
# i.e. gs = gridspec.GridSpec(1, 1)
# so that the same methods are available

fig = pyplot.figure()

ax = fig.add_subplot(gs[0, 0])

resolution = 20
path = 'C:/Users/jnieswand/Documents/Thesis/Data_master/Ground_truth_analysis/Resolution_'+str(resolution)+'/*/*/'
files = glob.glob( os.path.join(path, '*erroranalysis_cropped*') )
meansqu = np.array([])
method = np.array([])
scene = np.array([])
for file in files:
    s = 'standard deviation';
    with io.open(file, 'r') as f:
        for line in f:
            if 'mean relative error' in line:
                x = np.float(re.findall('[\\d.]+', line)[0])
                meansqu = np.append(meansqu, x)
                method = np.append(method, os.path.basename(os.path.split(os.path.split(file)[0])[0]))
                y = (re.findall('(.+)_refocus_correspondence', os.path.basename(os.path.split(file)[0]))[0])
                scene = np.append(scene, y)
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
indices = scene.argsort()
scene_set = set(scene[indices])
print(scene_set)
labelpos = np.array([])
tup = np.array([])
for k,x in enumerate(scene_set):
    data = meansqu[scene == x]
    i = np.arange(len(data)) + 5*k
    tup = np.append(tup, method[scene == x])
    ax.bar(i , data, width = 0.35, label = x)
    labelpos = np.append(labelpos, i)

plt.xticks(labelpos, tuple(tup) , rotation = 45, fontsize = 7, ha="right")
#red_patch = mpatches.Patch(color='red', label='The red data')
#red_patch = mpatches.Patch(color='blue', label='The red data')
#red_patch = mpatches.Patch(color='orange', label='The red data')
#red_patch = mpatches.Patch(color='purple', label='The red data')
#red_patch = mpatches.Patch(color='red', label='The red data')
ax.legend()
ax.set_ylabel('mean relative error')
pyplot.savefig('C:/Users/jnieswand/Documents/Thesis/Python_master/Plots/error_res'+str(resolution)+'_all')
pyplot.close()