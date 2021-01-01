from matplotlib import pyplot
import random

colors = ['red', 'green', 'blue', 'yellow', 'black']

while True:
    k = int(input())
    if k < 2 or k > 5:
        break
    with open('sample_data.txt-kmeans' + str(k) + '.txt', 'r') as f:
        k = int(f.readline())
        for i in range(k):
            n = int(f.readline())
            color = colors[i];
            for j in range(n):
                x, y = map(float, f.readline().split())
                pyplot.scatter(x=x, y=y, c=color, marker=('x' if j == 0 else 'o'))
        pyplot.show()
