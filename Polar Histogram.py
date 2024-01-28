import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

data = pd.read_csv("C:/Users/reina/Documents/Downloads/hapiness_report_2022.csv")
data = data.dropna(subset=['income'])

data_sorted = data.sort_values(by='score', ascending=False).reset_index(drop=True)

# Adjust theta values for the gap
n_points = len(data_sorted)
gap_radians = np.radians(10)
index_afghanistan = data_sorted.index[data_sorted['country'] == 'Afghanistan'][0]
index_finland = data_sorted.index[data_sorted['country'] == 'Finland'][0]
reduced_width = (2 * np.pi - gap_radians) / n_points
theta_reduced_width = np.linspace(0, 2 * np.pi - gap_radians, n_points, endpoint=False)
theta_with_10_degree_gap = np.array(
    [theta if (i < index_finland or i > index_afghanistan) else theta + gap_radians for i, theta in enumerate(theta_reduced_width)]
)

color_map_happiness = {
    'Low income': '#C26DBC',
    'Lower middle income': '#EEB5EB',
    'Upper middle income': '#C8F4F9',
    'High income': '#3CACAE'
}
colors_sorted_happiness = data_sorted['income'].map(color_map_happiness).tolist()
 
flags = {
    'Finland': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/finland.png"),
    'Denmark': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/denmark.png"),
    'Iceland': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/iceland.png"),
    'Switzerland': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/switzerland.png"),
    'Netherlands': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/netherlands.png"),
    'Luxembourg': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/luxembourg.png"),
    'Sweden': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/sweden.png"),
    'Norway': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/norway.png"),
    'New Zealand': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/new-zealand.png"),
    'Austria': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/austria.png"),
    'Australia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/australia.png"),
    'Ireland': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/ireland.png"),
    'Germany': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/germany.png"),
    'Canada': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/canada.png"),
    'United States': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/united-states.png"),
    'United Kingdom': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/united-kingdom.png"),
    'Czechia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/czechia.png"),
    'Belgium': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/belgium.png"),
    'France': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/france.png"),
    'Bahrain': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/bahrain.png"),
    'Slovenia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/slovenia.png"),
    'Costa Rica': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/costa-rica.png"),
    'United Arab Emirates': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/united-arab-emirates.png"),
    'Saudi Arabia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/saudi-arabia.png"),
    'Singapore': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/singapore.png"),
    'Romania': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/romania.png"),
    'Spain': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/spain.png"),
    'Uruguay': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/uruguay.png"),
    'Italy': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/italy.png"),
    'Kosovo': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/kosovo.png"),
    'Malta': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/malta.png"),
    'Lithuania': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/lithuania.png"),
    'Slovakia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/slovakia.png"),
    'Estonia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/estonia.png"),
    'Panama': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/panama.png"),
    'Brazil': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/brazil.png"),
    'Guatemala': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/guatemala.png"),
    'Kazakhstan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/kazakhstan.png"),
    'Cyprus': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/cyprus.png"),
    'Latvia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/latvia.png"),
    'Serbia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/serbia.png"),
    'Chile': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/chile.png"),
    'Nicaragua': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/nicaragua.png"),
    'Mexico': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/mexico.png"),
    'Croatia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/croatia.png"),
    'Poland': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/poland.png"),
    'El Salvador': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/el-salvador.png"),
    'Kuwait': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/kuwait.png"),
    'Hungary': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/hungary.png"),
    'Mauritius': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/mauritius.png"),
    'Uzbekistan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/uzbekistan.png"),
    'Japan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/japan.png"),
    'Honduras': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/honduras.png"),
    'Portugal': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/portugal.png"),
    'Argentina': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/argentina.png"),
    'Greece': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/greece.png"),
    'South Korea': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/south-korea.png"),
    'Philippines': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Philippines.png"),
    'Thailand': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Thailand.png"),
    'Moldova': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Moldova.png"),
    'Jamaica': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Jamaica.png"),
    'Kyrgyzstan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Kyrgyzstan.png"),
    'Belarus': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Belarus.png"),
    'Colombia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Colombia.png"),
    'Bosnia and Herzegovina': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Bosnia-and-Herzegovina.png"),
    'Mongolia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Mongolia.png"),
    'Dominican Republic': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Dominican-Republic.png"),
    'Malaysia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Malaysia.png"),
    'Bolivia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Bolivia.png"),
    'China': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/China.png"),
    'Paraguay': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Paraguay.png"),
    'Peru': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Peru.png"),
    'Montenegro': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Montenegro.png"),
    'Ecuador': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Ecuador.png"),
    'Vietnam': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Vietnam.png"),
    'Turkmenistan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Turkmenistan.png"),
    'Russia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Russia.png"),
    'Hong Kong': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Hong-Kong.png"),
    'Armenia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Armenia.png"),
    'Tajikistan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Tajikistan.png"),
    'Nepal': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Nepal.png"),
    'Bulgaria': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Bulgaria.png"),
    'Libya': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Libya.png"),
    'Indonesia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Indonesia.png"),
    'North Macedonia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/North-Macedonia.png"),
    'Albania': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Albania.png"),
    'South Africa': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/South-Africa.png"),
    'Azerbaijan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Azerbaijan.png"),
    'Gambia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Gambia.png"),
    'Bangladesh': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Bangladesh.png"),
    'Laos': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Laos.png"),
    'Algeria': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Algeria.png"),
    'Liberia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Liberia.png"),
    'Ukraine': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Ukraine.png"),
    'Morocco': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Morocco.png"),
    'Mozambique': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Mozambique.png"),
    'Cameroon': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Cameroon.png"),
    'Senegal': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Senegal.png"),
    'Niger': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Niger.png"),
    'Georgia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Georgia.png"),
    'Gabon': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Gabon.png"),
    'Iraq': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Iraq.png"),
    'Guinea': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Guinea.png"),
    'Iran': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Iran.png"),
    'Ghana': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Ghana.png"),
    'Turkey': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Turkey.png"),
    'Burkina Faso': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Burkina-Faso.png"),
    'Cambodia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Cambodia.png"),
    'Benin': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Benin.png"),
    'Comoros': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/Comoros.png"),
    'Uganda': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/uganda.png"),
    'Nigeria': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/nigeria.png"),
    'Kenya': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/kenya.png"),
    'Tunisia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/tunisia.png"),
    'Pakistan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/pakistan.png"),
    'Mali': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/mali.png"),
    'Namibia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/namibia.png"),
    'Eswatini': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/eswatini.png"),
    'Myanmar': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/myanmar.png"),
    'Sri Lanka': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/sri-lanka.png"),
    'Madagascar': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/madagascar.png"),
    'Egypt': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/egypt.png"),
    'Chad': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/chad.png"),
    'Ethiopia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/ethiopia.png"),
    'Yemen': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/yemen.png"),
    'Mauritania': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/mauritania.png"),
    'Jordan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/jordan.png"),
    'Togo': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/togo.png"),
    'India': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/india.png"),
    'Zambia': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/zambia.png"),
    'Malawi': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/malawi.png"),
    'Tanzania': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/tanzania.png"),
    'Sierra Leone': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/sierra-leone.png"),
    'Lesotho': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/lesotho.png"),
    'Botswana': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/botswana.png"),
    'Rwanda': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/rwanda.png"),
    'Zimbabwe': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/zimbabwe.png"),
    'Lebanon': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/lebanon.png"),
    'Afghanistan': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/afghanistan.png"),
    'Israel': Image.open("C:/Users/reina/Documents/Downloads/Rounded Country Flag_Complete/israel.png")

}

def resize_image(image, base_width):
    w_percent = base_width / float(image.size[0])
    h_size = int(float(image.size[1]) * float(w_percent))
    return image.resize((base_width, h_size), Image.ANTIALIAS)

flag_width = 50
for country in flags:
    flags[country] = resize_image(flags[country], flag_width)

# Plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(12, 12))
bars = ax.bar(theta_with_10_degree_gap, data_sorted['score'].values, width=reduced_width, 
              color=colors_sorted_happiness, edgecolor='white', linewidth=1.5)

# Hide boundary
ax.spines['polar'].set_visible(False)

# Make radial gridlines white
ax.yaxis.grid(color='white')

# Add labels to happiness scores on radial gridlines
label_frequency = 1 
max_score = max(data_sorted['score'])
for score in np.arange(0, max_score + label_frequency, label_frequency):
    radial_distance = score
    ax.text(0, radial_distance, f'{score:.1f}', color='orange', fontsize=7, ha='center', va='center')

# Add country names, guide lines, and flags
for theta_val, (country, score) in zip(theta_with_10_degree_gap, data_sorted[['country', 'score']].values):
    alignment = {}
    if 0 <= theta_val <= np.pi/2 or 3*np.pi/2 <= theta_val <= 2*np.pi:
        text_content = f"     ({score:.2f}) {country}"
    else:
        text_content = f"{country} ({score:.2f})     "
    if np.pi/2 < theta_val < 3*np.pi/2:
        alignment = {"ha": "right", "va": "center"}
        rotation_deg = theta_val*(180/np.pi) - 180
    else:
        alignment = {"ha": "left", "va": "center"}
        rotation_deg = theta_val*(180/np.pi)
    line_end_radial_distance = max(data_sorted['score'].values) + 0.38
    ax.plot([theta_val, theta_val], [score, line_end_radial_distance], color='orange', linestyle='--', linewidth=0.5)
    
    if country in flags:
        img = flags[country]
        offset_image = OffsetImage(img, zoom=0.25, resample=True)
        ab = AnnotationBbox(offset_image, (theta_val, max(data_sorted['score'].values) + 0.4),
                            frameon=False, boxcoords="data", pad=0.1, box_alignment=(0.5, 0.5))
        ax.add_artist(ab)
    
    ax.text(theta_val, max(data_sorted['score'].values) + 0.4, text_content, **alignment, rotation_mode="anchor",
            rotation=rotation_deg, fontsize=9, color="black")

# Legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_map_happiness[key], markersize=10) 
           for key in color_map_happiness]
legend = ax.legend(handles, color_map_happiness.keys(), loc='upper right', bbox_to_anchor=(1.3, 1.1))
for text in legend.get_texts():
    text.set_color("black")

ax.set_yticklabels([])
ax.set_xticks([])

fig.savefig("C:/Users/reina/Documents/Downloads/polarhisto2.svg", transparent=True, bbox_inches='tight', pad_inches=0.1)

plt.show()
