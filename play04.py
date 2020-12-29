import matplotlib.pyplot as plt
import numpy as np
import math

colors = ['r','cyan']

c0 = 'r'
c1 = 'cyan'

plt.figure(num='Whoa', figsize = (15,15))

z = 0.05
plt.plot([0.3+z,0.7+z],[0.3,0.3],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.3,0.7],[0.3,0.3],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.3+z,0.7+z],[0.7,0.7],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.3,0.7],[0.7,0.7],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.3+z,0.3+z],[0.3,0.7],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.3,0.3],[0.3,0.7],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.7+z,0.7+z],[0.3,0.7],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.7,0.7],[0.3,0.7],color=c1,alpha=0.1, linewidth=8)


z = 0.01
plt.plot([0.4+z,0.6+z],[0.4,0.4],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.4,0.6],[0.4,0.4],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.4+z,0.6+z],[0.6,0.6],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.4,0.6],[0.6,0.6],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.4+z,0.4+z],[0.4,0.6],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.4,0.4],[0.4,0.6],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.6+z,0.6+z],[0.4,0.6],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.6,0.6],[0.4,0.6],color=c1,alpha=0.1, linewidth=8)


plt.plot([0.35,0.41],[0.3,0.4],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.3,0.4],[0.3,0.4],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.35,0.41],[0.7,0.6],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.3,0.4],[0.7,0.6],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.75,0.61],[0.3,0.4],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.7,0.6],[0.3,0.4],color=c1,alpha=0.1, linewidth=8)

plt.plot([0.75,0.61],[0.7,0.6],color=c0,alpha=0.1, linewidth=8)
plt.plot([0.7,0.6],[0.7,0.6],color=c1,alpha=0.1, linewidth=8)


plt.axis('off')
plt.show()


