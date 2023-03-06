# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Define a function for the Standard map equations of motion

def standard_map(x, p, K):
    p_new = p + K*np.sin(x)
    x_new = (x + p_new) % (2*np.pi)
    return x_new, p_new

# Setup initial conditions

x0_1 = 3.0
p0_1 = 1.9

x0_2 = 3.0
p0_2 = 1.8999
K = 1.2
kicks_number = 50

# Create numpy arrays to store the trajectories values

x1 = np.zeros(kicks_number+1)
p1 = np.zeros(kicks_number+1)

x2 = np.zeros(kicks_number+1)
p2 = np.zeros(kicks_number+1)
x1[0] = x0_1
p1[0] = p0_1

x2[0] = x0_2
p2[0] = p0_2

# Update the trajectories

for n in range(kicks_number):
    x1[n+1], p1[n+1] = standard_map(x1[n], p1[n], K)
    x2[n+1], p2[n+1] = standard_map(x2[n], p2[n], K)

# Create two plot/subplot

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(np.arange(kicks_number+1), x1, label='x')
axs[0].plot(np.arange(kicks_number+1), p1, label='p')
axs[0].set_xlabel('Kick number n')
axs[0].set_ylabel('Value')
axs[0].set_title(f'Trajectory 1: (x0, p0) = ({x0_1}, {p0_1})')
axs[0].legend()
axs[1].plot(np.arange(kicks_number+1), x2, label='x')
axs[1].plot(np.arange(kicks_number+1), p2, label='p')
axs[1].set_xlabel('Kick number n')
axs[1].set_ylabel('Value')
axs[1].set_title(f'Trajectory 2: (x0, p0) = ({x0_2}, {p0_2})')
axs[1].legend()
plt.show()
