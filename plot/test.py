import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("plot/data.csv")
fig, ax = plt.subplots()

for idx, (_, row) in enumerate(df.iterrows()):
    x = row.to_numpy()[1:-1]
    y = np.loadtxt(df.keys()[1:-1])
    ax.plot(x, y, linewidth=1,
            color=(0, 0, 0.5, (10+idx)/100))
plt.gca().invert_yaxis()
ax.set_yticks(np.insert(y, 0, 0))
plt.show()
