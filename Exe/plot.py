'''
将数据域的所有特征的变化趋势，输出到一张图中
'''
from pandas import read_csv
from matplotlib import pyplot
# load dataset
dataset = read_csv('F:/Research_Project/DataSet/0b_decimal/0x545.csv', header=0, index_col=0)
values = dataset.values[:500]
# specify columns to plot
groups = [0, 1, 2, 3,4, 5, 6,7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()