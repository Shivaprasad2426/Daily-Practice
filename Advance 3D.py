import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Creating a 3D spiral spring plot
theta = np.linspace(0, 4 * np.pi, 100)
z = np.linspace(0, 1, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title("3D Spiral Spring")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_spiral_spring.png")
plt.show()

# Creating a 3D surface plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title("3D Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_surface_plot.png")
plt.show()

# Creating a 3D wireframe plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='blue')
ax.set_title("3D Wireframe Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_wireframe_plot.png")
plt.show()

# Creating a 3D contour plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(x, y, z, 50, cmap='viridis')
ax.set_title("3D Contour Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_contour_plot.png")
plt.show()

# Creating a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=z, cmap='viridis')
fig.colorbar(scatter)
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_scatter_plot.png")
plt.show()

# Creating an animated 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(num, x, y, z, line):
    ax.clear()
    ax.plot(x[:num], y[:num], z[:num])
    ax.set_title("Animated 3D Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

line, = ax.plot(x, y, z)
ani = FuncAnimation(fig, update, frames=len(x), fargs=[x, y, z, line], interval=100)
ani.save('animated_3D_plot.gif', writer='imagemagick')

plt.show()

# Creating a 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
_x, _y = np.meshgrid(np.arange(4), np.arange(3))
x, y = _x.ravel(), _y.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)
ax.set_title("3D Bar Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_bar_plot.png")
plt.show()

# Creating a 3D quiver plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.meshgrid(np.arange(-1, 1, 0.2),
                      np.arange(-1, 1, 0.2),
                      np.arange(-1, 1, 0.8))
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.1)
ax.set_title("3D Quiver Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_quiver_plot.png")
plt.show()

# Creating a 3D streamplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Y, Z = np.mgrid[-3:3:100j, -3:3:100j]
X = Y**2 - Z**2

u = -1 - X**2 + Y
v = 1 + X - Y**2
w = 1 + X + Z**2

ax.streamplot(X, Y, Z, u, v, w)
ax.set_title("3D Streamplot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_streamplot.png")
plt.show()

# End of the advanced 3D visualizations and animations program
