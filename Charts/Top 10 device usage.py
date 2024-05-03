import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
warnings.filterwarnings("ignore")

# Load data from csv file
df = pd.read_csv('../Netflix.csv', sep=';')

# Reducing name length

df['Device Type'].replace('Apple iPad Pro 12.9in 4th Gen (Wi-Fi) iPad', 'iPad Pro', inplace=True)
df['Device Type'].replace('Apple iPhone 13 Mini', 'iPhone 13 Mini', inplace=True)
df['Device Type'].replace('Netflix Windows App - Cadmium Windows Mobile', 'Windows Mobile', inplace=True)
df['Device Type'].replace('DefaultWidevineAndroidPhone', 'Android Phone', inplace=True)
df['Device Type'].replace('Google Chromecast V3 Streaming Stick', 'Google Chromecast', inplace=True)
df['Device Type'].replace('Android DefaultWidevineL3Tablet Android Tablet', 'Android Tablet', inplace=True)

# Grouping the data

data = df['Device Type'].value_counts().sort_values(ascending=False)[:10]


color_map = ['#221f1f' for _ in range(11)]
color_map[0] = color_map[1] = '#ff5722'  # color highlight

# Initialize the figure

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.axis('off')

# Constants = parameters controlling the plot layout:

upperLimit = 1400
lowerLimit = 90
labelPadding = 30

# Compute max in the dataset

max = data.max()

# Compute heights: they are a conversion of each item value in those new coordinates

slope = (max - lowerLimit) / max
heights = slope * data.values + lowerLimit

# Compute the width of each bar. In total, we have 2*Pi = 360°

width = 2 * np.pi / len(data.index)

# Compute the angle each bar is centered on:

indexes = list(range(1, len(data.index) + 1))
angles = [element * width for element in indexes]

# Draw bars

bars = ax.bar(
    x=angles,
    height=heights,
    width=width,
    bottom=lowerLimit,
    linewidth=2,
    edgecolor="white",
    color=color_map, alpha=0.8
)

# Add labels

for bar, angle, height, label in zip(bars, angles, heights, data.index):

    # Labels are rotated. Rotation must be specified in degrees

    rotation = np.rad2deg(angle)

    # Flip some labels upside down

    alignment = ""
    if np.pi / 2 <= angle < 3 * np.pi / 2:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"

    # Add the labels

    ax.text(
        x=angle,
        y=lowerLimit + bar.get_height() + labelPadding,
        s=label,
        ha=alignment, fontsize=10, fontfamily='serif',
        va='center',
        rotation=rotation,
        rotation_mode="anchor")

plt.show()
