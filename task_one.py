import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('x_y_coordinates.txt', delimiter=',', header=None, names=['x', 'y'])

print("Column names:", data.columns.tolist())
plt.figure(figsize=(8, 6))
plt.scatter(data['x'], data['y'], color='blue', alpha=0.7, label='Coordinates')
plt.title('Scatter Plot of Coordinates')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
