import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#task1
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x² - 4x + 4")
plt.grid()
plt.show()

#task2
x = np.linspace(0, 2*np.pi, 400)

plt.figure()
plt.plot(x, np.sin(x), linestyle='--', marker='o', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='-', marker='x', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid()
plt.show()

#task3
x = np.linspace(0, 2, 400)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, x**3)
plt.title("f(x) = x³")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x))
plt.title("f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x))
plt.title("f(x) = eˣ")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2, 2, 4)
plt.plot(x, np.log(x + 1))
plt.title("f(x) = log(x+1)")
plt.xlabel("x")
plt.ylabel("y")

plt.tight_layout()
plt.show()

#task4
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Scatter Plot")
plt.grid()
plt.show()

#task5
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution")
plt.show()
#task6

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, Z)
fig.colorbar(surface)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Surface Plot of cos(x² + y²)")

plt.show()

#task7
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()

#task8
labels = ['T1', 'T2', 'T3', 'T4']
cat_a = [20, 35, 30, 35]
cat_b = [25, 32, 34, 20]
cat_c = [15, 20, 25, 30]

x = np.arange(len(labels))

plt.figure()
plt.bar(x, cat_a, label='Category A')
plt.bar(x, cat_b, bottom=cat_a, label='Category B')
plt.bar(x, cat_c, bottom=np.array(cat_a) + np.array(cat_b), label='Category C')

plt.xticks(x, labels)
plt.xlabel("Time Period")
plt.ylabel("Value")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()
