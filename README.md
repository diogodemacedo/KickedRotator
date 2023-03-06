## Standard Map Simulation

This repository contains a Python script for simulating the Standard map, a well-known discrete-time dynamical system in chaos theory. The script allows the user to generate phase space plots for both single and multiple trajectories. In plasma physics, these phase space plots can be used to study the behavior of charged particles, such as electrons or ions, as they move in a magnetic field. By simulating the motion of these particles over time, researchers can gain insights into various plasma phenomena, such as turbulence, transport, and wave-particle interactions.

## Scripts

**`standardmap_trajectories.py`**: This script simulates the trajectories of two points in the standard map/kicked rotator model and generates a plot with the trajectories, under a given number of kicks. Input values: x0_1 and p0_1(initial values of the first point in the map), x0_2 and p0_2: (initial values of the second point in the map); K (the strength of the perturbation in the map); kicks_number (the number of iterations (or "kicks") to perform).

**`phase_portrait.py`**: This script generates phase space plots for single and multiple trajectories of the standard map/kicked rotator model.

### Applications

This script can be further developed to include additional features that are relevant to plasma physics research. For example,this script can be used to generate data that can be analyzed using machine learning techniques, such as clustering or classification algorithms, to identify patterns in the phase space plots that could reveal insights into plasma behavior. Additionally, its possible to use this script to simulate the dynamics of charged particles in more complex magnetic field geometries, such as tokamaks or stellarators.
