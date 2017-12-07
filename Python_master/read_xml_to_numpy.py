# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:41:07 2017

@author: jnieswand
"""

def read_xml_to_numpy(path):
    import numpy as np
    import xml.etree.ElementTree as ET

    for event, node in ET.iterparse(path):
        if node.tag == 'rows':
            rows = np.int(node.text)
        if node.tag == 'cols':
            cols = np.int(node.text)
        if node.tag == 'data':
            fl_line = [[np.float(x) for x in line.split()] for line in node.text.splitlines()]
            out = np.reshape(np.array(fl_line[1:]), (rows,cols))
    return(out)

if __name__ == '__main__':
    arr = read_xml_to_numpy("C:/Users/jnieswand/Desktop/Data_master/pixel_response/complex_res1/depth_"+str(1)+".xml")
    import matplotlib.pylab as plt
    im = plt.imshow(arr, cmap='hot')