#python -m pip install matplotlib
import matplotlib.pyplot as plt

def plot_polygon(points):
    Xs = [i[0] for i in points] + [points[0][0]]
    Ys = [i[1] for i in points] + [points[0][1]]
    plt.plot(Xs, Ys)

def betweens(points, m):
    Xs = [i[0] for i in points] + [points[0][0]]
    Ys = [i[1] for i in points] + [points[0][1]]

    result = []
    for i in range(len(points)):
        new_x = (Xs[i]*m + Xs[i + 1]) / (m + 1)
        new_y = (Ys[i]*m + Ys[i + 1]) / (m + 1)
        result.append((new_x, new_y))
    return result

#changable:
hexagon = [[0,  10],
       [-8.66,  5],
       [-8.66, -5],
       [0, -10],
       [ 8.66, -5],
       [ 8.66,  5],
       [ 0,  10]]

#you can change 150 and 10
for i in range(150):
    plot_poly(hexagon)
    hexagon = betweens(hexagon, 10)

plt.show()  
