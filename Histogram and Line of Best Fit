import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load data
data = pd.read_csv("C:/Users/reina/Documents/Downloads/hapiness_report_2022_cleaned.csv")

# Use plasma colormap in matplotlib
color_map = plt.cm.plasma

# Calculate the mean & std of happiness scores
mu, std = norm.fit(data['score'])

# Enhanced Typography and Figure Size
plt.figure(figsize=(12,7))

# Plot the histogram with plasma colormap
n, bins, patches = plt.hist(data['score'], bins=20, rwidth=0.8, density=False, alpha=0.75, edgecolor='white')

# Color code each bin based on its position
col = (bins[:-1] - min(bins[:-1])) / (max(bins[:-1]) - min(bins[:-1]))
for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', color_map(c))

# Adjust axes
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#666666')
ax.spines['left'].set_color('#666666')

# Adjust y-axis labels to intervals of 2
max_ylim = max([patch.get_height() for patch in patches])
ax.set_yticks(range(0, int(max_ylim) + 1, 2))

# Define x values for the line of best fit
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Plot the line of best fit with a darker shade of green (#006400), tgt with a dotted style
p = norm.pdf(x, mu, std) * len(data['score']) * (bins[1] - bins[0])
plt.plot(x, p, '#006400', linewidth=2, linestyle=':')

# Annotate with mean with dashed/dotted line 
plt.axvline(mu, color='red', linestyle='dashed', linewidth=1)
plt.text(mu*0.87, max_ylim*0.95, 'Mean: {:.2f}'.format(mu), color='red', fontsize=14)

# Data Labels
for i in range(len(patches)):
    height = patches[i].get_height()
    if height > 0:
        plt.text(patches[i].get_x() + patches[i].get_width() / 2., height + 0.5, 
                 f"{int(height)}", ha="center", va="bottom", fontsize=12, color='black')

# Title and Subtitle
plt.title('Distribution of Happiness Scores (2022)', fontsize=18, fontweight='bold', color='#333333', y=1.2)

# Axis labels
plt.xlabel('Happiness Score', fontsize=14, color='#333333')
plt.ylabel('Number of Countries', fontsize=14, color='#333333')

plt.tight_layout()

# Change the grid style
plt.grid(axis='y', linestyle='-.', linewidth=0.5, alpha=0.5)

# Save figure as an SVG with a transparent background
plt.savefig("C:/Users/reina/Documents/Downloads/distribution_bar_chart.svg", transparent=True, format="svg")

# Display the plot
plt.show()
