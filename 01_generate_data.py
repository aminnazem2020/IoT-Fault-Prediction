import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 2000
timestamps = pd.date_range('2024-01-01', periods=n_samples, freq='H')

data = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': np.random.normal(60, 5, n_samples),
    'vibration': np.random.normal(2, 0.4, n_samples),
    'pressure': np.random.normal(30, 3, n_samples),
})

# Simulate faults: sudden increases
data['fault'] = ((data['temperature'] > 68) & (data['vibration'] > 2.4)).astype(int)

data.to_csv('data/sensor_data.csv', index=False)
print("✅ Synthetic IoT sensor data generated.")
