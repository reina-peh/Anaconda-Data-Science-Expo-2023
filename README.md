# Anaconda Data Science Expo 2023

> **Achievement:**  
> 1st Place Overall & $7,000 USD

This competition was organized by Anaconda, the world's most popular data science platform. It was held at National University of Singapore (NUS), where both [Anaconda](https://www.anaconda.com/) from the United States and [AI Singapore](https://aisingapore.org/) jointly carried out 2 rounds of judging. 

# Overview 
I have used Jupyter Notebook, a web-based computing platform, to code and generate a total of 9 charts to compete under the data visualization category of this competition. This repository contains my finalized codes for a total of 8 charts shown in the poster below:

![Anaconda Research Poster (1)](https://github.com/risingcupcakes/Anaconda-Data-Science-Expo-2023/assets/75836749/673ae96b-2381-4e04-bc3a-505c56f4ee4e)

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
!pip install pandas matplotlib seaborn scipy numpy plotly geopandas
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

# Challenges
### 1. Creation of a links structure
The primary technical challenge in generating the Sankey diagram was creating a structured list of dictionaries that define links between nodes. 

#### Our solution:
```
# Extract the matrix data
matrix_inc = df_inc.iloc[:, 1:].values.tolist()
names_inc = df_inc.columns[1:].tolist()

# Construct the links DataFrame using list comprehension
data_inc = [{'source': names_inc.index(name), 'target': names_inc.index(target_name), 'value': matrix_inc[i][j]} 
            for i, name in enumerate(names_inc) 
            for j, target_name in enumerate(names_inc) if matrix_inc[i][j] > 0]
```
We achieved the desired format by using a list comprehension to iterate over the extracted matrix data, transforming it into a list `data_inc` where each element is a dictionary representing a link between two nodes (countries). The comprehension `for i, name in enumerate(names_inc)` iterates over each country name to establish it as the source node, while a nested loop `for j, target_name in enumerate(names_inc)` determines each target node. The key `'source'` is set to `names_inc.index(name)`, leveraging the `index()` function to translate the country name to its corresponding index in the `names_inc` list. Likewise, the `'target'` key is assigned the index of the target country, and the `'value'` key holds the migration flow from the source to the target extracted from `matrix_inc[i][j]`. In short, this indexing and mapping method converts country names into numerical indices that are used to draw the links between nodes, thereby representing the flow of migrants between different income-level countries.

# Contributors
* Reina Peh [LinkedIn](https://www.linkedin.com/in/reinapeh/)
* Ryan Tan [LinkedIn](https://www.linkedin.com/in/ryantzr/)
* Claudia Lai [LinkedIn](https://www.linkedin.com/in/claudialaijy/)

