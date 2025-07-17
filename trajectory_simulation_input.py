import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
air_resistance = 0.01  # Air resistance coefficient
dt = 0.01  # Time step (s)
total_time = 10  # Total simulation time (s)

# Take user input for velocity and angle
v0 = float(input("Enter initial velocity (m/s): "))
angle_deg = float(input("Enter launch angle (degrees): "))
angle_rad = np.radians(angle_deg)

# Initial velocity components
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# Lists to store the trajectory points
x_vals = [0]
y_vals = [0]

# Initial positions
x = 0
y = 0

# Simulation loop
for _ in np.arange(0, total_time, dt):
    # Calculate magnitude of velocity
    v = np.sqrt(vx**2 + vy**2)

    # Calculate drag forces
    fx = -air_resistance * v * vx
    fy = -air_resistance * v * vy - g  # Include gravity in y-direction

    # Update velocity components
    vx += fx * dt
    vy += fy * dt

    # Update positions
    x += vx * dt
    y += vy * dt

    # Break if missile hits the ground
    if y < 0:
        break

    # Append new positions to the lists
    x_vals.append(x)
    y_vals.append(y)

# Plotting the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label=f"v0 = {v0} m/s, angle = {angle_deg}°")
plt.title("Missile Trajectory Simulation with Air Resistance")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.legend()
plt.show()
