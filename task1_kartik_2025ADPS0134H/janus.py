import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# loads data from csv file using pandas library 

FILE = "Raw_Test_Flight_Data_25.csv"
COL = "Pressure (Pa)"
dt = 1.0  # time delay

# reads CSV file

df = pd.read_csv(FILE)
pressure = pd.to_numeric(df[COL], errors="coerce").fillna(
    method="bfill").fillna(method="ffill").to_numpy()
time = np.arange(len(pressure)) * dt

# finds values of altitude using pressure with the help of formula

P0, T0, g, M, R = 101325, 288.15, 9.80665, 0.0289644, 8.3144598
altitude = (T0 * R / (M * g)) * np.log(P0 / pressure)

# smooths the graph by taking average because the data obtained from the raw file and calculations provides a cary ragged graph


def moving_avg(arr, window=5):
    return pd.Series(arr).rolling(window=window, center=True, min_periods=1).mean().to_numpy()


alt_smooth = moving_avg(altitude, window=5)

# computes velocity with the help of numpy library 

velocity = np.gradient(alt_smooth, dt)

# animated graph setup with the help of matplotlib

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# plots data using matplotlib 

ax1.set_title("Altitude vs Time (Smoothed)")
ax1.set_ylabel("Altitude (m)")
ax2.set_title("Velocity vs Time (Smoothed)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Vertical Velocity (m/s)")

alt_line, = ax1.plot([], [], color="blue", lw=2)
vel_line, = ax2.plot([], [], color="red", lw=2)

ax1.set_xlim(0, max(time))
ax1.set_ylim(min(alt_smooth)-10, max(alt_smooth)+10)
ax2.set_xlim(0, max(time))
ax2.set_ylim(min(velocity)-10, max(velocity)+10)

# animation functions


def init():
    alt_line.set_data([], [])
    vel_line.set_data([], [])
    return alt_line, vel_line


def update(i):
    alt_line.set_data(time[:i], alt_smooth[:i])
    vel_line.set_data(time[:i], velocity[:i])
    return alt_line, vel_line

#sets time interval

ani = FuncAnimation(fig, update, init_func=init, frames=len(
    time), interval=400, blit=True, repeat=False)

plt.tight_layout()
plt.show()

