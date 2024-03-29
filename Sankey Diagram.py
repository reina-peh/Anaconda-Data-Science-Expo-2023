import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.io as pio

df_inc = pd.read_excel("C:/Users/reina/Documents/Downloads/undesa_destination_and_origin_processed.xlsx", sheet_name="International Migrant Flow_Inc")
df_inc.columns = df_inc.iloc[0]
df_inc = df_inc.drop(0)
df_inc.reset_index(drop=True, inplace=True)

# Matrix data
matrix_inc = df_inc.iloc[:, 1:].values.tolist()
names_inc = df_inc.columns[1:].tolist()

# Links DataFrame using list comprehension
data_inc = [{'source': names_inc.index(name), 'target': names_inc.index(target_name), 'value': matrix_inc[i][j]} 
            for i, name in enumerate(names_inc) 
            for j, target_name in enumerate(names_inc) if matrix_inc[i][j] > 0]

source = [link['source'] for link in data_inc]
target = [link['target'] for link in data_inc]
value = [link['value'] for link in data_inc]

# Define my color palette to match the dataset labels
color_map = {
    'Low-income countries': '#C26DBC',
    'Lower-middle-income countries': '#EEB5EB',
    'Upper-middle-income countries': '#C8F4F9',
    'High-income countries': '#3CACAE'
}

node_colors = [color_map.get(name, '#D3D3D3') for name in names_inc]
link_colors = [node_colors[src] for src in source]

fig_custom_hover = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = names_inc,
      color = node_colors,
      hovertemplate = '<b>%{label}</b><br>Total Value: %{value}'
    ),
    link = dict(
      source = source,
      target = target,
      value = value,
      color = link_colors
    )
)])

fig_custom_hover.update_layout(
    font=dict(size=100, family="Arial Bold"),
    title_text="International Migrant Flow (Income-based)"
)

fig_custom_hover.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig_custom_hover.update_layout(title_text="International Migrant Flow (Income-based)", font_size=16)
fig_custom_hover.show()

svg_file_path = "C:/Users/reina/Documents/Downloads/sankey_diagram_transparent.svg"
pio.write_image(fig_custom_hover, svg_file_path, format="svg")

