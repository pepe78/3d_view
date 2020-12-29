import matplotlib.pyplot as plt
import numpy as np
import math

colors = ['r','cyan']

c0 = 'r'
c1 = 'cyan'

plt.figure(num='Whoa', figsize = (15,15))

n = 0
while True:
    plt.clf()

    z1 = 0.05 * math.cos(n * 2.0 * math.pi / 50.0)
    plt.plot([0.3+z1,0.7+z1],[0.3,0.3],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.3,0.7],[0.3,0.3],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.3+z1,0.7+z1],[0.7,0.7],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.3,0.7],[0.7,0.7],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.3+z1,0.3+z1],[0.3,0.7],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.3,0.3],[0.3,0.7],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.7+z1,0.7+z1],[0.3,0.7],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.7,0.7],[0.3,0.7],color=c1,alpha=0.1, linewidth=8)


    z2 = 0.01
    plt.plot([0.4+z2,0.6+z2],[0.4,0.4],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.4,0.6],[0.4,0.4],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.4+z2,0.6+z2],[0.6,0.6],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.4,0.6],[0.6,0.6],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.4+z2,0.4+z2],[0.4,0.6],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.4,0.4],[0.4,0.6],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.6+z2,0.6+z2],[0.4,0.6],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.6,0.6],[0.4,0.6],color=c1,alpha=0.1, linewidth=8)


    plt.plot([0.3+z1,0.4+z2],[0.3,0.4],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.3,0.4],[0.3,0.4],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.3+z1,0.4+z2],[0.7,0.6],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.3,0.4],[0.7,0.6],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.7+z1,0.6+z2],[0.3,0.4],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.7,0.6],[0.3,0.4],color=c1,alpha=0.1, linewidth=8)

    plt.plot([0.7+z1,0.6+z2],[0.7,0.6],color=c0,alpha=0.1, linewidth=8)
    plt.plot([0.7,0.6],[0.7,0.6],color=c1,alpha=0.1, linewidth=8)


    plt.axis('off')
    #plt.savefig(f"./tmp/im_{n:04d}.png")
    plt.draw()
    plt.pause(0.01)        
    
    n += 1

