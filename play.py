import matplotlib.pyplot as plt
import numpy as np

colors = ['r','cyan']

plt.figure(num='Whoa', figsize = (15,15))

for i in range(8):
    circle1=plt.Circle((0.1 + i * 0.1, 0.1 + i * 0.1),.1,color='r',alpha=0.1)
    plt.gcf().gca().add_artist(circle1)
    circle1=plt.Circle((0.1 + i * 0.1 + 0.01 + 0.01 * i, 0.1 + i * 0.1),.1,color='cyan',alpha=0.1)
    plt.gcf().gca().add_artist(circle1)

plt.axis('off')
plt.show()

