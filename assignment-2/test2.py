from matplotlib import pyplot
import csv

with open('data.csv') as f:
    file_csv = csv.reader(f)
    l = [float(l[0]) for l in file_csv]
    pyplot.hist(l, range=(0, 100), bins=20)
    pyplot.show()
