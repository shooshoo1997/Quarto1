import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
plt.figure(2)
plt.scatter(df['Duration'], df['Pulse'])
plt.show()