import pandas as pd
import numpy as np

# Creating a DataFrame from scratch (Simulation of staging data)
data = {
    'emp_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['DE', 'DS', 'DE', 'DA'],
    'salary': [95000, 105000, np.nan, 88000] # Simulated missing value
}
df = pd.DataFrame(data)