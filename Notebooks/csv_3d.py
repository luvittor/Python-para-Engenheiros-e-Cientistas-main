# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:37:50 2023

@author: luvit
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def csv_3d(file_path):
    df = pd.read_csv(file_path, header=None, engine = 'python')

    del df[0]
    del df[1]
    del df[2]

    x = df[3].values.tolist()
    y = df[4].values.tolist()
    z = df[5].values.tolist()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    return ax.scatter(x,y,z)