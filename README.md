# Anaconda Data Science Expo 2023
> **Achievement 🏆 :**  
> 1st Place Overall & $7,000 USD

This competition was organized by Anaconda, the world's most popular data science platform. It was held in Singapore, at the National University of Singapore (NUS), where both [Anaconda](https://www.anaconda.com/) from the United States and [AI Singapore](https://aisingapore.org/) jointly carried out 2 rounds of judging. 

# Decoding Happiness With Python
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8.10-green)
![IDE](https://img.shields.io/badge/IDE-Jupyter%20Notebook-orange)
![Anaconda Research Poster (4)](https://github.com/reina-peh/Anaconda-Data-Science-Expo-2023/assets/75836749/feec8f96-585e-4eed-a0cd-ca3c6184f6af)  
The exploration of the happiness topic stems from a profound curiosity to decode the intricate factors that contribute to our overall well-being and contentment. In our quest to understand this complex emotion and universal pursuit, we analyzed 5 datasets and visualized regional-level insights about happiness by coding 8 static and interactive charts using Python. We then weaved our charts and insights into a visual narrative (see poster) which tells its data-driven story about happiness! 🌻  

# Contributors 
* Reina Peh 
* Ryan Tan 
* Claudia Lai 

# Datasets
Refer to the `Datasets` folder to download the following datasets:
* social_progress_dataset
* DataForTable2.1WHR2023 
* undesa_destination_and_origin_processed 
* hapiness_report_2022 
* Regions  

# Installation
To install the required Python libraries/packages in your Jupyter Notebook, run:
```
!pip install pandas matplotlib seaborn scipy numpy plotly kaleido geopandas
```
This will install the following libraries along with their dependencies:

`Pandas`: An open-source data analysis and manipulation tool  
`Matplotlib`: A comprehensive library for creating static, animated, and interactive visualizations in Python   
`Seaborn`: A statistical data visualization library built on top of matplotlib  
`Scipy`: An open-source Python library used for scientific and technical computing  
`Numpy`: The fundamental package for scientific computing with Python  
`Plotly`: An interactive graphing library for Python  
`Kaleido`: For static image export support with Plotly  
`Geopandas`: An open-source project that makes working with geospatial data in python easier  

# Charts 
* Polar Histogram
* Choropleth Map
* Histogram with KDE
* Radar Chart
* Boxplot
* Sankey Diagram
* Bar Chart
* Scatterplot

# Challenges We Faced
### 1. Creation of a links structure
The `go.Sankey` function consists of 2 parameters `node (dict)` and `link (dict)`. The primary technical challenge in generating the Sankey diagram was constructing the inputs for sub-parameters `source`, `target` and `value` in the `link (dict)` parameter. And the inputs required an advanced DataFrame that the function could interpret.

#### Our Approach:
```
matrix_inc = df_inc.iloc[:, 1:].values.tolist()
names_inc = df_inc.columns[1:].tolist()

data_inc = [{'source': names_inc.index(name), 'target': names_inc.index(target_name), 'value': matrix_inc[i][j]} 
            for i, name in enumerate(names_inc) 
            for j, target_name in enumerate(names_inc) if matrix_inc[i][j] > 0]
```
We achieved the desired format by using a list comprehension to iterate over our extracted matrix data, transforming it into a list `data_inc` where each element is a dictionary representing a link between two nodes (countries). The comprehension `for i, name in enumerate(names_inc)` iterates over each country name to establish it as the source node, while a nested loop `for j, target_name in enumerate(names_inc)` determines each target node. The key `'source'` is set to `names_inc.index(name)`, leveraging the `index()` function to translate the country name to its corresponding index in the `names_inc` list. 

Likewise, the `'target'` key is assigned the index of the target country, and the `'value'` key holds the migration flow from the source to the target extracted from `matrix_inc[i][j]`. In short, this indexing and mapping method converts country names into numerical indices that are used to draw the links between nodes, thereby representing the flow of migrants between different income-level countries.  


### 2. Positioning customization of 2-part texts
In developing the polar histogram, we encountered with challenges with positioning the country names and scores as such: `<score> <country>` for the right hemisphere and `<country> <score>` for the left hemisphere of the plot, while also aligning and rotating with the positions of the data points. 

#### Our Approach:
``` 
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
```
The code first determines the text content's sequence `text_content` based on the angular position `theta_val` of the data point. For data points in the right hemisphere (0 to π/2 and 3π/2 to 2π radians), the text is formatted as `<score> <country>`. For points in the left hemisphere (π/2 to 3π/2 radians), it's `<country> <score>`. Depending on whether the data point is in the left or right hemisphere, the horizontal alignment `ha` is set to "right" or "left", respectively. This ensures that the text is aligned in a way that it's always outward-facing from the center of the plot, enhancing readability (vertical alignment `va` is consistently set to "center"). 

The rotation of the text `rotation_deg` is calculated based on `theta_val`, with an adjustment of - 180 degrees when the point is in the left hemisphere. This rotation aligns the text with the radial lines of the plot, ensuring that the text orientation is consistent with the direction of the data points.  


Thank you for reading! 😊



