import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# Load data from csv file
df = pd.read_csv('../Netflix.csv', sep=';')


# Format the Title column and Duration column

df['Title'] = df['Title'].str.split(':').str[0]  # Remove the episode information from the Title column
df['Duration'] = pd.to_timedelta(df['Duration'])  # Convert the Duration column to timedelta

# Compute the total watch time for each title

df['Total Watch Time'] = df['Duration'].dt.total_seconds() / 3600  # Convert the Duration to hours
top_titles = df.groupby('Title')['Total Watch Time'].sum().sort_values(ascending=False)[:10]

# Plot

color_map = ['#f5f5f1' for _ in range(10)]
color_map[0] = color_map[1] = color_map[2] = '#ff5722'  # color highlight

fig, ax = plt.subplots(1, 1, figsize=(24, 18))
ax.bar(top_titles.index, top_titles, width=0.5,
       edgecolor='darkgray',
       linewidth=1.2, color=color_map)

# annotations
for i in top_titles.index:
    ax.annotate(f"{round(top_titles[i])}",
                xy=(i, top_titles[i] + 6.75),
                va='center', ha='center', fontsize=20, fontweight='light', fontfamily='serif')

# Remove border from plot

for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Title and subtitle

fig.text(0.09, 0.96, 'Top 10 most watched movies/series', fontsize=30, fontweight='bold', fontfamily='serif')
fig.text(0.09, 0.91, 'The three most watched movies/series have been highlighted.', fontsize=24, fontweight='light',
         fontfamily='serif')

ax.grid(axis='y', linestyle='-', alpha=0.4)
plt.xticks(range(len(top_titles)), top_titles.index, rotation='vertical')
grid_y_ticks = np.arange(0, 180, 20)  # y ticks, min, max, then step
ax.set_yticks(grid_y_ticks)

ax.set_axisbelow(True)

# Axis labels

# plt.xlabel("Month", fontsize=12, fontweight='light', fontfamily='serif', loc='center', y=-1.5)
plt.ylabel("Duration (Hours)", fontsize=24, fontweight='light', fontfamily='serif', loc='center', x=-1.5)

# Show plot
ax.tick_params(axis=u'both', which=u'both', length=0)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=20)

plt.show()
