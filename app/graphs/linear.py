import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def linear_graph(dataframe, label1, label2, value1, value2, components, selected_components, name_colum, graph_type):
    filtered_data = dataframe[(dataframe[label1] == value1) & (dataframe[label2] == value2)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    num_colors = len(components) + len(selected_components)
    colors = plt.cm.get_cmap('tab20', num_colors)
    if graph_type == "N":
        x = filtered_data[name_colum]
        for idx, component in enumerate(components):
            if component in filtered_data.columns:
                y = filtered_data[component]
                ax1.plot(x, y, label=component, color=colors(idx))
        ax1.set_xlabel(name_colum)
        ax1.set_ylabel('Mols')
        ax1.grid(True)

    elif graph_type == "T":
        x = filtered_data['Temperature']
        for idx, component in enumerate(components):
            if component in filtered_data.columns:
                y = filtered_data[component]
                ax1.plot(x, y, label=component, color=colors(idx))
        ax1.set_xlabel('Temperature')
        ax1.set_ylabel('Mols')
        ax1.grid(True)

    elif graph_type == "P":
        x = filtered_data['Pressure']
        for idx, component in enumerate(components):
            if component in filtered_data.columns:
                y = filtered_data[component]
                ax1.plot(x, y, label=component, color=colors(idx))
        ax1.set_xlabel('Pressure')
        ax1.set_ylabel('Mols')
        ax1.grid(True)
    
    ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

    if selected_components:
        if graph_type == "N":
            label = name_colum
            x = filtered_data[label]
        elif graph_type == "T":
            label = 'Temperature'
            x = filtered_data[label]
        elif graph_type == "P":
            label = 'Pressure'
            x = filtered_data[label]

        selected_data = filtered_data[selected_components]
        total_sum = selected_data.sum(axis=1)
        normalized_data = selected_data.div(total_sum, axis=0)
        
        for idx, component in enumerate(selected_components):
            if component in normalized_data.columns:
                y = normalized_data[component]
                ax2.plot(x, y, label=f"{component}", color=colors(idx))
        
        ax2.set_xlabel(label)
        ax2.set_ylabel('Molar Fraction')
        ax2.grid(True)
        ax2.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
    
    plt.tight_layout()
    plt.show()