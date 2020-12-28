import matplotlib.pyplot as plt
import numpy as np
import math

colors = ['r','cyan']

# solar system - first is sun (made smaller) - this is highly unprecise and not calibrated
# just for fun purposes
# https://www.bobthealien.co.uk/solarsystem/table.htm
planetDist = np.array([0, 0.036, 0.067, 0.092, 0.141, 0.483, 0.888, 1.783, 2.797]) * 0.4
planetSize = np.array([.01, 0.03, 0.07, 0.08, 0.04, 0.89, 0.75, 0.32, 0.31]) * 0.2

# these numbers were heavily modified (and not precise at all)
planetTime = np.array([1., 88., 224., 365., 687., 112., 129., 184., 165.]) * 0.02
planetPos  = np.random.rand(9) * 2.0 * math.pi

plt.figure(num='Whoa', figsize = (15,15))

time = 0
num = 0
while True:
    plt.clf()
    
    
    for i in range(len(planetDist)):
        XX = planetDist[i] * math.cos(planetPos[i] + 2.0 * math.pi * time / planetTime[i])
        YY = planetDist[i] * math.sin(planetPos[i] + 2.0 * math.pi * time / planetTime[i])
    
        x = XX + 0.5
        y = -YY * 0.6 + 0.5
        z = YY * 0.4 + 0.5

        circle1=plt.Circle((x - z * 0.07, y), planetSize[i] * (1.4 + YY) * 0.2,color='cyan',alpha=0.1 if i != 0 else 0.3)
        plt.gcf().gca().add_artist(circle1)
        circle1=plt.Circle((x + z * 0.07, y), planetSize[i] * (1.4 + YY) * 0.2,color='r',alpha=0.1 if i != 0 else 0.3)
        plt.gcf().gca().add_artist(circle1)

    plt.axis('off')
    #plt.savefig(f"./tmp/im_{num:04d}.png")
    plt.draw()
    plt.pause(0.01)        

    time += 0.1 
    num += 1
