import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_excel('cbsafactbook2021.xlsx')
x_axis = file['Core Based Statistical Area (CBSA)']
y_axis = file['2010 Population']
plt.bar(x_axis, y_axis, width=5)
plt.xlabel("Cities")
plt.ylabel("Population")
plt.show()