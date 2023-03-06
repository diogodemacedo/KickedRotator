#Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Define the Standard map function #same as exercise 1

def standard_map(x, p, K):
    p_new = p + K*np.sin(x)
    x_new = (x + p_new) % (2*np.pi)
    return x_new, p_new
    
    

# Define a function to generate a phase space plot for a single trajectory

def plot_trajectory(x0, p0, K, num_kicks):

    # Initialize arrays to store the trajectory
    x = np.zeros(num_kicks+1)
    p = np.zeros(num_kicks+1)
    x[0] = x0
    p[0] = p0

    # Calculate the trajectory
    for n in range(num_kicks):
        x[n+1], p[n+1] = standard_map(x[n], p[n], K)

    # Plot the trajectory in phase space
    plt.plot(x % (2*np.pi), p % (2*np.pi), '.')
    plt.xlabel('x (mod 2*pi)')
    plt.ylabel('p (mod 2*pi)')
    plt.title(f'Trajectory: (x0, p0) = ({x0}, {p0}), K = {K}')
    plt.show()

# Define a function to generate a phase space plot for multiple trajectories

def plot_phase_space(K, num_trajectories):

    # Generate random initial conditions for each trajectory
    np.random.seed(1234)
    x0_list = np.random.uniform(0, 2*np.pi, num_trajectories)
    p0_list = np.random.uniform(0, 2*np.pi, num_trajectories)

    # Initialize arrays to store the trajectories
    x = np.zeros((num_trajectories, num_kicks+1))
    p = np.zeros((num_trajectories, num_kicks+1))
    x[:,0] = x0_list
    p[:,0] = p0_list

    # Calculate the trajectories
    for n in range(num_kicks):
        x[:,n+1], p[:,n+1] = standard_map(x[:,n], p[:,n], K)

    # Plot the phase space portrait
    fig, ax = plt.subplots()
    for i in range(num_trajectories):
        ax.plot(x[i,:] % (2*np.pi), p[i,:] % (2*np.pi), '.', alpha=0.5)
    ax.set_xlabel('x (mod 2*pi)')
    ax.set_ylabel('p (mod 2*pi)')
    ax.set_title(f'Phase space portrait: K = {K}')
    plt.show()

# Set the parameters for the single trajectory test

x0 = 3.0
p0 = 1.9
K = 1.2
num_kicks = 1000

# Generate a phase space plot for a single trajectory

plot_trajectory(x0, p0, K, num_kicks)

# Set the parameters for the multiple trajectory test

K_list = [1.2, 2.1, 5.5]
num_trajectories = 100

# Generate a phase space plot for each value of K

for K in K_list:
    plot_phase_space(K, num_trajectories)

