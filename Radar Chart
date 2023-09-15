import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
regions_df = pd.read_excel("C:/Users/reina/Documents/Downloads/Regions.xlsx")
social_progress_df = pd.read_excel("C:/Users/reina/Documents/Downloads/social_progress_dataset.xlsx")

# Set correct headers for the social progress dataset
social_progress_df.columns = social_progress_df.iloc[1]
social_progress_df = social_progress_df.drop(index=[0, 1])

# Filter the social progress dataframe to only include rows for the years 2013-2022
filtered_social_progress_df = social_progress_df[social_progress_df['SPI \nyear'].between(2013, 2022)]

# Convert metric columns to numeric
metrics = ["Nutrition & Basic Medical Care", "Water & Sanitation", "Shelter", "Personal Safety", "Access to Basic Knowledge", "Access to Information & Communications", "Health & Wellness ", "Environmental Quality", "Personal Rights", "Personal Freedom & Choice", "Inclusiveness", "Access to Advanced Education"]

for metric in metrics:
    filtered_social_progress_df[metric] = pd.to_numeric(filtered_social_progress_df[metric], errors='coerce')

# Compute the 10-year average for each metric for each country
average_metrics_df = filtered_social_progress_df.groupby('Country')[metrics].mean().reset_index()

# Merge the average metrics dataframe with the regions dataframe
merged_df = average_metrics_df.merge(regions_df, on='Country', how='left')

# Compute the 10-year average for each metric by region
regional_averages_df = merged_df.groupby('Region')[metrics].mean().reset_index()

# Define function for plotting
def plot_radar_chart(data, metrics, title):
    N = len(metrics)
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    # Close plot by appending the first value to the end of the data series
    theta = np.concatenate([theta, [theta[0]]])
    
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': 'polar'})
    ax.set_title(title, y=1.08, fontsize=18)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    plt.xticks(theta, metrics + [metrics[0]], color='black', size=12, ha='center', va='center')
    ax.set_rlabel_position(255)
    ax.spines['polar'].set_color('black')
    ax.set_facecolor((0, 0, 0, 0))
    plt.yticks([25, 50, 75, 100], ["25", "50", "75", "100"], color="black", size=12)
    plt.ylim(0, 100)
    
    color_palette = ['#339F00', '#0500FF', '#9CDADB', '#FF00DE', '#FF9900', '#FFFFFF']

    for idx, (i, row) in enumerate(data.iterrows()):
        values = row[metrics].values.flatten().tolist()
        # Close the plot for each data series by appending the first value to the end
        values = values + [values[0]]
        ax.plot(theta, values, linewidth=1.75, linestyle='solid', label=row['Region'], color=color_palette[idx % len(color_palette)])
        ax.fill(theta, values, alpha=0.50, color=color_palette[idx % len(color_palette)])
        # Add dots to the vertices of the radar chart
        ax.plot(theta, values, marker='o', markersize=10, color=color_palette[idx % len(color_palette)])
        
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1)) 
    
    # Return the 'fig' object for saving
    return fig


# Plot the radar chart
fig = plot_radar_chart(regional_averages_df, metrics, title="10-Year Average Metrics by Region (2013-2022)")
plt.tight_layout()

# Save the figure
fig.savefig("C:/Users/reina/Documents/Downloads/radar_Basic Human Needs.svg", format="svg", transparent=True)

# Show the plot
plt.show()
