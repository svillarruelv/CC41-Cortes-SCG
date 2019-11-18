import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sets(order, prisms):
    x = []
    y = []
    z = []
    dx = []
    dy = []
    dz = []
    for i in range(len(prisms)):
        if prisms[i].sheet == order:
            x.append(prisms[i].x)
            y.append(prisms[i].y)
            z.append(prisms[i].z)
            dx.append(prisms[i].w)
            dy.append(prisms[i].h)
            dz.append(prisms[i].l)
    return x, y, z, dx, dy, dz

def graph(order, _prisms):
    fig = plt.figure()
    if order>1:
        axs=[None]*order
        for i in range(order):
            num = 100+order*10+i+1
            axs[i] = fig.add_subplot(num, projection='3d')
        for i in range(len(axs)):
            x, y, z, dx, dy, dz = sets(i+1, _prisms)
            axs[i].bar3d(x, y, z, dx, dy, dz, color = '#FFE714C0', shade=True)
            axs[i].set_title('Contenedor '+str(i+1))    
    else:
        ax1 = fig.add_subplot(111, projection='3d')
        ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color = '#FFE714C0', shade=True)
        ax1.set_title('Contenedor 1')

    plt.show()
