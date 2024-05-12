from pandas import read_csv
from matplotlib.pyplot import figure, scatter, title, xlabel, ylabel, grid, show

data = read_csv('x_y_coordinates.txt', delimiter=',', header=None, names=['x', 'y'])

print("Data structure:", data.columns.tolist())

fig = figure()
scatter(data['x'], data['y'])
title('Coordinate Scatter Plot')
xlabel('X Axis')
ylabel('Y Axis')
grid()
show()
