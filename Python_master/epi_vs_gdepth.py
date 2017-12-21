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

fig = pyplot.figure(figsize=(10,10))

ax = fig.add_subplot(gs[0, 0])

masked = False
with_gt = True
if with_gt:
    add = "_w_gt"
else:
    add = "";
if masked:
    path = 'C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure'+add+'/EXTENDED_error_analysis/*/'
else:
    path = 'C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure'+add+'/*refocus*/'
files = glob.glob( os.path.join(path, 'final*erroranalysis_cropped*') )
path2 = 'C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure'+add+'/*basic*/'
files = files + glob.glob( os.path.join(path2, '*erroranalysis_cropped*'))
meansqu = np.array([])
method = np.array([])
scenes = np.array([])
for file in files:
    s = 'standard deviation';
    with io.open(file, 'r') as f:
        y = re.findall('(.+)_refocus_correspondence', os.path.basename(os.path.split(file)[0]))
        if len(y)>0:
            scene = y[0]
        else:
            scene = re.findall('(.+)_basicST', os.path.basename(os.path.split(file)[0]))[0]
        for line in f:
            if 'mean relative error' in line and scene !='tiltplane':
                x = np.float(re.findall('[\\d.]+', line)[0])
                meansqu = np.append(meansqu, x)
                method = np.append(method, re.findall(scene+'_(.+)', os.path.basename(os.path.split(file)[0]))[0])
                scenes = np.append(scenes, scene)
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
indices = scenes.argsort()
scene_set = set(scenes[indices])
print(scene_set)
labelpos = np.array([])
tup = np.array([])
for k,x in enumerate(scene_set):
    data = meansqu[scenes == x]
    i = np.arange(len(data)) + 5*k
    tup = np.append(tup, method[scenes == x])
    ax.bar(i , data, width = 0.35, label = x)
    labelpos = np.append(labelpos, i)

plt.xticks(labelpos, tuple(tup) , rotation = 45, fontsize = 10, ha="right")
#red_patch = mpatches.Patch(color='red', label='The red data')
#red_patch = mpatches.Patch(color='blue', label='The red data')
#red_patch = mpatches.Patch(color='orange', label='The red data')
#red_patch = mpatches.Patch(color='purple', label='The red data')
#red_patch = mpatches.Patch(color='red', label='The red data')
ax.legend()
ax.set_ylabel('mean relative error')
pyplot.savefig('C:/Users/jnieswand/Documents/Thesis/Python_master/Plots/epi_vs_gdepth_masked_'+str(masked) + add)
pyplot.close()