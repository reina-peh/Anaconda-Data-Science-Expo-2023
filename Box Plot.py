import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

regions_df = pd.read_excel("C:/Users/reina/Documents/Downloads/Regions.xlsx")
data_df = pd.read_excel("C:/Users/reina/Documents/Downloads/social_progress_dataset.xlsx")

regions_dict = regions_df.set_index('Country').to_dict()['Region']
data_df['Region'] = data_df['Country'].map(regions_dict)
data_df = data_df.dropna(subset=['Region'])

# 10-year averages
averaged_df = data_df.groupby(['Country', 'Region']).mean().reset_index()

melted_df = pd.melt(averaged_df, id_vars=['Country', 'Region'], value_vars=['Basic Human Needs', 'Foundations of Wellbeing', 'Opportunity'], var_name='Metric', value_name='Score')

# Adjust region ordering
correct_region_order = ['Americas', 'Pacific', 'Europe', 'Sub-Saharan Africa', 'Middle East and North Africa', 'Asia']

# Create a bit of space between regions in the data for better visualization
region_space = 1
dodge_factor = 0.32
melted_df_spaced = melted_df.copy()
for i, region in enumerate(correct_region_order[:-1]):
    next_region_index = melted_df[melted_df['Region'] == correct_region_order[i + 1]].index.min()
    space_df = pd.DataFrame({'Country': ' ', 'Region': ' ', 'Metric': melted_df['Metric'].unique(), 'Score': [None, None, None]})
    melted_df_spaced = pd.concat([melted_df_spaced.iloc[:next_region_index + region_space * i], space_df, melted_df_spaced.iloc[next_region_index + region_space * i:]]).reset_index(drop=True)

sns.set_style("whitegrid")
palette = ['#0099FF', '#00E600', '#D500F9']

fig, ax = plt.subplots(figsize=(24, 12))

fig.patch.set_facecolor('white')
ax.set_facecolor('white')

sns.boxplot(data=melted_df_spaced, x="Region", y="Score", hue="Metric", ax=ax, palette=palette, dodge=True, width=0.5, fliersize=5, boxprops=dict(alpha=.7), order=correct_region_order)
sns.swarmplot(data=melted_df_spaced, x="Region", y="Score", hue="Metric", ax=ax, palette=palette, dodge=dodge_factor, marker="o", size=5, edgecolor="gray", linewidth=0.5, alpha=0.7, order=correct_region_order)

ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.set_title("Distribution of Social Progress Scores (2013-2022) by Region", fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel("Region", fontsize=16, fontweight='bold', labelpad=15)
ax.set_ylabel("Score", fontsize=16, fontweight='bold', labelpad=15)
ax.tick_params(axis='both', which='major', labelsize=14, pad=10)
ax.set_xticklabels(correct_region_order, rotation=0, horizontalalignment='center', fontsize=14)
ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

# World averages
ax.axhline(averaged_df['Basic Human Needs'].mean(), color=palette[0], linestyle='--', linewidth=2, alpha=0.8)
ax.axhline(averaged_df['Foundations of Wellbeing'].mean(), color=palette[1], linestyle='--', linewidth=2, alpha=0.8)
ax.axhline(averaged_df['Opportunity'].mean(), color=palette[2], linestyle='--', linewidth=2, alpha=0.8)

ax.text(5.5, averaged_df['Basic Human Needs'].mean() + 0.5, f"Average: {averaged_df['Basic Human Needs'].mean():.2f}", color=palette[0], fontsize=15, verticalalignment='center')
ax.text(5.5, averaged_df['Foundations of Wellbeing'].mean() + 0.5, f"Average: {averaged_df['Foundations of Wellbeing'].mean():.2f}", color=palette[1], fontsize=15, verticalalignment='center')
ax.text(5.5, averaged_df['Opportunity'].mean() - 1, f"Average: {averaged_df['Opportunity'].mean():.2f}", color=palette[2], fontsize=15, verticalalignment='center')

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:3], labels[:3], title="Metric", loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12, title_fontsize=14, frameon=False)

fig.tight_layout(pad=2)
plt.show()

fig.savefig("C:/Users/reina/Documents/Downloads/box_plot.svg", format='svg', dpi=1200, transparent=True)

