import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv','r')
df.plot()
plt.show()
