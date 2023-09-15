import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
happiness_data = pd.read_csv("C:/Users/reina/Documents/Downloads/hapiness_report_2022_cleaned.csv")
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
print(happiness_data.columns)

# Fetch names of all countries in 'naturalearth_lowres' dataset
country_names = world['name'].tolist()
print(country_names)

# Merge datasets with an 'outer' join to identify unmatched entries
merged_data = world.merge(happiness_data, left_on="name", right_on="country", how="outer", indicator=True)

# Extract unmatched entries from 2022 happiness dataset
unmatched_countries = merged_data[merged_data['_merge'] == 'right_only']['country']
print(unmatched_countries)

# Update 'Country name' column to replace "United States" with "United States of America"
happiness_data['country'] = happiness_data['country'].replace("United States", "United States of America")
happiness_data['country'] = happiness_data['country'].replace("Bosnia and Herzegovina", "Bosnia and Herz.")
happiness_data['country'] = happiness_data['country'].replace("Dominican Republic", "Dominican Rep.")
happiness_data['country'] = happiness_data['country'].replace("Eswatini", "eSwatini")
world = world.merge(happiness_data, left_on="name", right_on="country", how="left")

# Adjust x and y-axis limits
x_min_limit = world[world['name'] == 'Russia'].geometry.bounds.minx.min() + 10
y_min = -60
y_max = 90

# Set up color palette and plot
color_map = plt.cm.plasma

# Define a function to determine text color based on happiness score
def get_text_color(score):
    # Define threshold value for color change
    threshold = (world['score'].max() + world['score'].min()) / 2
    return 'white' if score < threshold else 'black'

fig, ax = plt.subplots(1, 1, figsize=(20, 12))

# Plot choropleth map with specified color gradient
world.boundary.plot(ax=ax, linewidth=1, color='black')
world.plot(column='score', linewidth=0.8, ax=ax, edgecolor='black',
           vmin=world['score'].min(), vmax=world['score'].max(),
           legend=True, legend_kwds={'label': "Happiness Score", 'orientation': "horizontal", 'pad': 0.01, 'shrink': 0.3},
           missing_kwds={'color': 'lightgrey'}, cmap=color_map)

# Label other countries with only their scores
for x, y, score in zip(world.geometry.representative_point().x, world.geometry.representative_point().y, world['score']):
    if pd.notna(score):
        ax.text(x, y, f"{score:.2f}", fontsize=8, ha='center', va='center', color=get_text_color(score))

# Adjust x and y-axis limits for the shift to the right
ax.set_xlim(x_min_limit, None)
ax.set_ylim(y_min, y_max)

# Remove axes and title the plot
ax.axis('off')
plt.title('World Happiness Score (2022)', fontsize=16)

# Save my plot as an SVG with a transparent background
output_file_path = "C:/Users/reina/Documents/Downloads/world_happiness_map_2022.svg"
plt.savefig(output_file_path, transparent=True, format="svg")

output_file_path
