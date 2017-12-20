import numpy as np
import os
import glob
import io
import re
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


class parameter():
    def __init__(self):
        self.min_disp = 5
        self.max_disp = 9
        self.px = 1050.0
        self.b_mm = 18.0
        self.sensor_width = 32.0
        self.disp_offset = 0
        self.resolution_per_pixel = 10
    def labelToDisparity(self,i):
        return( (self.max_disp- self.min_disp)/(self.resolution_per_pixel * 
               self.max_disp- self.min_disp +1)* i + self.min_disp)
p = parameter()
xvalue = "200"
yvalue = "200"
path = 'C:/Users/jnieswand/Desktop/Data_master/pixel_response/complex_res10'
files = glob.glob( os.path.join(path, 'pixelvalue*'+yvalue+'_'+xvalue+'*') )

ax1.set_xlabel("Disparity (px)")
ax1.set_ylabel("Response magnitude")
ax1.set_title("x = "+xvalue+", y = "+yvalue)
for file in files:
    print(file)
    data = np.loadtxt(file)
    x = np.arange(0, len(data))
    ax1.plot(p.labelToDisparity(x), data, label = file[87:-12])
ax1.legend()
pyplot.savefig("C:/Users/jnieswand/Desktop/Python_master/Plots/Pixel_response/x"+xvalue+"y"+yvalue+".png")
pyplot.close()  # releases the memeory