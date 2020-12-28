import matplotlib.pyplot as plt
import numpy as np
import math

colors = ['r','cyan']

plt.figure(num='Whoa', figsize = (15,15))

time = 0
num = 0
while True:
    plt.clf()
    
    
    for i in range(1,9,2):
        z = 0.07 + 0.07 * math.cos(time * i * 0.1 + i)
        circle1=plt.Circle((0.1 + i * 0.1 - z * 0.5, 0.1 + i * 0.1),.03,color='cyan' if z >= 0 else 'r',alpha=0.1)
        plt.gcf().gca().add_artist(circle1)
        circle1=plt.Circle((0.1 + i * 0.1 + z * 0.5, 0.1 + i * 0.1),.03,color='r' if z >= 0 else 'cyan',alpha=0.1)
        plt.gcf().gca().add_artist(circle1)

    plt.axis('off')
    #plt.savefig(f"./tmp/im_{num:04d}.png")
    plt.draw()
    plt.pause(0.01)        

    time += 0.1 
    num += 1
