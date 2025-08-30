# This repository contains solutions for the given problem statements.  
Below is a brief overview of how each question was tackled.


*files included:
1)task1_kartik_2025ADPS0134H
2)updated_task2cide_kartik_2025ADPS0134H
3)task2_kartik_2025ADPS0134H
4)README.txt




*Task 1: Surprising Galactus's Planning

This project filters raw test-flight data to examine altitude and velocity profiles of a launched prototype. The aim is to retrieve pressure readings, determine altitude, remove noisy data, calculate velocity, and graph animated output for enhanced visualization.


->Problem Statement
Reed intends to detonate a bomb directly upward towards Galactus' face and detonate it at the height of the trajectory of the bomb. In order to analyze the movement profile, flight pressure data is examined to calculate altitude and velocity with respect to time.


->Steps Taken

1.Data Loading
- Imported raw pressure data from Raw_Test_Flight_Data_25.csv with pandas.
- Dealt with missing or damaged values with forward and backward fill techniques.

2.Altitude Calculation
- Transformed pressure values to altitude via the barometric formula:
 
3.Noise Reduction
- Applied moving average smoothing to the altitude data for noise reduction due to sensor errors.

4. Velocity Calculation
- Computed the vertical velocity based on the gradient of the smoothed altitude array.

5. Data Visualization
- Plotted Altitude vs Time and Velocity vs Time graphs.
- Utilized Matplotlib and FuncAnimation to animate the graphs.


-> Features
- Smoothes out noisy sensor data with a rolling average.
- Shows animated graphs for improved visualization.
- Properly handles missing or corrupted pressure readings.

->libraries used
- numpy
- pandas
- matplotlib



*Task 2: State Detection and Indication using Arduino

This project simulates a rocket's movement phases using a force sensor, LED indicators, and a piezo buzzer on tinkercad. The LEDs display the current state of the device, and the buzzer sounds at the peak (apogee). Data smoothing is applied using a moving average to reduce noise from the force sensor.

-> Problem Statement
- Detect the device's state:
- Indicate the state using different LED colors.
- Activate a buzzer at the peak(apogee).
- Simulate everything on Tinkercad using available components


 1. Components Used
- Arduino Uno
- Force Sensor
- LEDs (3 for states)
- Piezo Buzzer
- Resistors and Breadboard

2. Working Logic
- Read sensor data from the force sensor via analog pin A0.
- Apply a moving average filter to smooth noisy readings.
- Maintain previous readings (s and `) to detect trends:
  - If avg < s and s < q → Descending (LED 1 ON)
  - If avg == s → Apogee (LED 2 ON)
  - If avg > s → Ascending (LED 3 ON)
- At apogee, buzzer beeps for 300 ms at 1 kHz.

 3. Noise Reduction
- Implemented a sliding window moving average with size 3 for stable readings.


->Features
- LED indicators for ascent, peak, and descent.
- Buzzer alert at apogee.
- moving average smoothing for noisy sensor signals.



-> used Arduino IDE (Tinkercad).

