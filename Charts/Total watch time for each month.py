import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
warnings.filterwarnings("ignore")

# Load data from csv file
df = pd.read_csv('../Netflix.csv', sep=';')

# Helper column for various plots
df['count'] = 1

# Format the 'Duration' column and Start Time column
df['Duration'] = pd.to_timedelta(df['Duration'])
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Filter the data for 2022
data_2022 = df[df['Start Time'].dt.year == 2022]
data = df.groupby('Duration')['count'].sum().sort_values(ascending=False)[:5]

monthly_duration_2022 = data_2022.groupby(data_2022['Start Time'].dt.month)['Duration'].sum().sort_values(
    ascending=False)
monthly_duration_2022 = monthly_duration_2022.dt.total_seconds() / 3600

# Plot

color_map = ['#f5f5f1' for _ in range(12)]
color_map[0] = color_map[1] = color_map[2] = '#ff5722'  # color highlight

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.bar(monthly_duration_2022.index, monthly_duration_2022, width=0.5,
       edgecolor='darkgray',
       linewidth=0.6, color=color_map)

# annotations
for i in monthly_duration_2022.index:
    ax.annotate(f"{round(monthly_duration_2022[i])}",
                xy=(i, monthly_duration_2022[i] + 2),
                va='center', ha='center', fontweight='light', fontfamily='serif')

# Remove border from plot

for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Title and subtitle

fig.text(0.09, 0.96, 'Total Watch Time for each month', fontsize=15, fontweight='bold', fontfamily='serif')
fig.text(0.09, 0.91, 'The three months with highest watch time have been highlighted.', fontsize=12, fontweight='light',
         fontfamily='serif')

ax.grid(axis='y', linestyle='-', alpha=0.4)

grid_x_ticks = np.arange(1, 13, 1)  # x ticks, min, max, then step
ax.set_xticks(grid_x_ticks)
grid_y_ticks = np.arange(0, 45, 5)  # y ticks, min, max, then step
ax.set_yticks(grid_y_ticks)

ax.set_axisbelow(True)

# Axis labels

plt.xlabel("Month", fontsize=12, fontweight='light', fontfamily='serif', loc='center', y=-1.5)
plt.ylabel("Duration (Hours)", fontsize=12, fontweight='light', fontfamily='serif', loc='center', x=-1.5)

# Show plot
ax.tick_params(axis=u'both', which=u'both', length=0)

plt.show()
