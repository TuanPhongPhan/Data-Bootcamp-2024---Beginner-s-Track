import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

plt.rcParams['figure.dpi'] = 140
# Load data from csv file
df = pd.read_csv('../Netflix.csv', sep=';')

# Helper column for various plots
df['count'] = 1

# Bar plot showing how many entries there are for each country

data = df.groupby('Country')['count'].sum().sort_values(ascending=False)[:5]

# Plot

color_map = ['#f5f5f1' for _ in range(10)]
color_map[0] = color_map[1] = color_map[2] = '#ff5722'  # color highlight

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.bar(data.index, data, width=0.5,
       edgecolor='darkgray',
       linewidth=0.6, color=color_map)

# annotations
for i in data.index:
    ax.annotate(f"{data[i]}",
                xy=(i, data[i] + 150),
                va='center', ha='center', fontweight='light', fontfamily='serif')

# Remove border from plot

for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Title and subtitle

fig.text(0.09, 0.96, 'Number of Entries for Each Country', fontsize=15, fontweight='bold', fontfamily='serif')

ax.grid(axis='y', linestyle='-', alpha=0.4)

grid_y_ticks = np.arange(0, 6000, 500)  # y ticks, min, max, then step
ax.set_yticks(grid_y_ticks)
ax.set_axisbelow(True)

# thicken the bottom line
plt.axhline(y=0, color='black', linewidth=1.3, alpha=.7)

ax.tick_params(axis='both', which='major', labelsize=12)

# Show plot
ax.tick_params(axis=u'both', which=u'both', length=0)

plt.show()


