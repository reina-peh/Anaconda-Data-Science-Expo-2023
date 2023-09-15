import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

regions_df = pd.read_excel("C:/Users/reina/Documents/Downloads/Regions.xlsx", engine='openpyxl')
data_df = pd.read_excel("C:/Users/reina/Documents/Downloads/social_progress_dataset.xlsx", engine='openpyxl')

regions_dict = regions_df.set_index('Country').to_dict()['Region']
data_df['Region'] = data_df['Country'].map(regions_dict)
data_df = data_df.dropna(subset=['Region'])

# 10-year averages
averaged_df = data_df.groupby(['Country', 'Region']).mean().reset_index()

merged_df = averaged_df.merge(regions_df, on="Country", how="left")
colors = {
    'Americas': '#1f77b4',
    'Asia Pacific': '#ff7f0e',
    'Europe': '#2ca02c',
    'Middle East/Africa': '#d62728'
}

def plot_regression_line(ax, x, y, color):
    slope, intercept, r_value, _, _ = stats.linregress(x, y)
    x_vals = np.linspace(min(x), max(x), 100)
    y_vals = slope * x_vals + intercept
    ax.plot(x_vals, y_vals, color=color, linewidth=2, alpha=0.8)
    return r_value

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
plt.rcParams['axes.facecolor'] = 'none'
plt.grid(color='#ffffff', linestyle='-', linewidth=0.5)

metrics = ['Basic Human Needs', 'Foundations of Wellbeing', 'Opportunity']
for i, metric in enumerate(metrics):
    ax = axes[i]
    for region, color in colors.items():
        idx = merged_df['Region'] == region
        ax.scatter(merged_df[metric][idx], merged_df['Social Progress Index'][idx], 
                   c=color, label=region, alpha=0.7, marker='o', s=60)
    plot_regression_line(ax, merged_df[metric], merged_df['Social Progress Index'], '#333333')
    ax.set_title(f'SPI vs {metric}', fontsize=14)
    ax.set_ylabel('Social Progress Index', fontsize=12)
    ax.set_xlabel(metric, fontsize=12)

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='center right', fontsize='medium')

plt.tight_layout()
plt.subplots_adjust(right=0.85)
file_path = "C:/Users/reina/Documents/Downloads/social_progress_scatter_plots.svg"
plt.savefig(file_path, format='svg', transparent=True)
plt.close(fig)

