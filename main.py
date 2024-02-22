import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile_motion(initial_velocity, launch_angle, gravity=9.8, time_step=0.1, total_time=10):
    launch_angle_rad = np.radians(launch_angle)
    initial_velocity_x = initial_velocity * np.cos(launch_angle_rad)
    initial_velocity_y = initial_velocity * np.sin(launch_angle_rad)

    time_points = np.arange(0, total_time, time_step)
    x_positions = initial_velocity_x * time_points
    y_positions = initial_velocity_y * time_points - 0.5 * gravity * time_points ** 2

    return x_positions, y_positions


initial_velocity = int(input("Enter initial Velocity"))  # meters per second
launch_angle = int(input("Enter launch angle")) # degrees
x, y = simulate_projectile_motion(initial_velocity, launch_angle)

plt.plot(x, y)
plt.title(f'Projectile Motion Simulation for {initial_velocity} and {launch_angle}')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.show()

