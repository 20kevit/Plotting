import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x, y, r = 0, 0, 1

for i in range(50):
    ax.add_patch(plt.Circle((x,y), r, color = "r", fill=False))
    y -= 0.005
    r -= 0.005
    ax.add_patch(plt.Circle((x,y), r, color = "g", fill=False))
    x -= 0.005
    r -= 0.005
    ax.add_patch(plt.Circle((x,y), r, color = "b", fill=False))
    y += 0.005
    r -= 0.005
    ax.add_patch(plt.Circle((x,y), r, color = "y", fill=False))
    x += 0.005
    r -= 0.005
plt.show()
