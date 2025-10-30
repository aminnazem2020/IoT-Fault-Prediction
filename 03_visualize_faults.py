import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/sensor_data.csv')

plt.figure(figsize=(12,6))
plt.plot(data['timestamp'], data['temperature'], label='Temperature', alpha=0.6)
plt.plot(data['timestamp'], data['vibration'], label='Vibration', alpha=0.6)
plt.scatter(data.loc[data['fault'] == 1, 'timestamp'],
            data.loc[data['fault'] == 1, 'temperature'],
            color='red', label='Fault', marker='x')

plt.legend()
plt.title("Machine Sensor Data with Fault Points")
plt.xlabel("Time")
plt.ylabel("Sensor Values")
plt.tight_layout()
plt.show()
