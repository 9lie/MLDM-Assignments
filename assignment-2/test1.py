from matplotlib import pyplot
import csv

with open('data.csv') as f:
    file_csv = csv.reader(f)
    for l in file_csv:
        pyplot.scatter(float(l[0]), float(l[-1]))
    pyplot.show()
