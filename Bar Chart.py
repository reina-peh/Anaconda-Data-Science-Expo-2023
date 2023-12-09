import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/reina/Documents/Downloads/hapiness_report_2022_cleaned.csv")

# Sort dataset by score and select the top 5, bottom 5 & middle 10 countries 
df_sorted = df.sort_values(by='score', ascending=True)
top_5 = df_sorted.head(5)
bottom_5 = df_sorted.tail(5)
middle_10 = df_sorted.iloc[len(df_sorted)//2 - 5 : len(df_sorted)//2 + 5]
data = pd.concat([top_5, middle_10, bottom_5])
print(data)

colors_updated = ['#FFCF00']*5 + ['#ED6879']*10 + ['#800080']*5

# Set length for white bars to 10
white_bar_length = 10

# Create plot
plt.figure(figsize=(15,10), facecolor='none')

# Plot white bars
plt.barh(data['country'], white_bar_length, color='white', height=0.6, edgecolor='lightgray')

# Plot colored bars on top of white bars
bars = plt.barh(data['country'], data['score'], color=colors_updated[::-1], height=0.6)

# Remove vertical axis while keeping labels
plt.gca().axes.get_yaxis().set_ticks_position('none')

# Add scores at the end of bars
for bar, score in zip(bars, data['score']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{score:.3f}', 
             va='center', ha='right', color=bar.get_facecolor(), weight='bold')

plt.title('Happiness Scores of Selected Countries (2022)')

 # Remove grid lines
plt.grid(False) 

# Save plot as SVG with transparent background
plt.savefig("C:/Users/reina/Documents/Downloads/bar_chart.svg", format='svg', transparent=True, bbox_inches='tight')

plt.show()
