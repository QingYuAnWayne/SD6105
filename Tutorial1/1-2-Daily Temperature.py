# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:17:07 2021

CZ4124 Data Visualisation (Tutorial 1 Template)
@author: Zhang Xuwei
 
"""

import matplotlib.pyplot as plt
import pandas as pd

PlotWithPandas = True  # you can plot either with Pandas or Matplotlib
#---------------------------------------------------------------------
# Read in Daily Temperature datafile into dataframe Temp
#---------------------------------------------------------------------
Temp = pd.read_csv('Daily_Temperature.csv')  # change to your directory
print('\nTable read in\n',Temp,'\n')

#---------------------------------------------------------------------
# Use MELT to covert to long form and apply column names
#---------------------------------------------------------------------
# put in your code here
temp_table = Temp.melt(id_vars="Name",var_name="Day", value_name="Temp")
print('\nafter melt is\n',temp_table,'\n')


#---------------------------------------------------------------------
# Use PIVOT to convert to wide form with Names in each column
#---------------------------------------------------------------------
# put in your code here
temp_table = temp_table.pivot(
    index="Day", columns="Name", values="Temp"
)
new_index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp_table = temp_table.reindex(new_index)
print('\nafter pivot is\n',temp_table,'\n')


#-------------------------------
# Use Pandas to plot line chart
#-------------------------------
if(PlotWithPandas):
    print('\nPlotting with Pandas')
    # put your Pandas plotting code here
    line_plot = temp_table.plot(title="Daily Temperature for each Student")
    # Line style: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    # axhline: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html
    line_plot.set_ylabel("Temperature(Celsius)")
    line_plot.axhline(y=38.0, color="red", linestyle="dashed")
    line_plot.axhline(y=37.0, color="green", linestyle="dashed")
    plt.show()

    
#----------------------------------
# Use Matplotlib to plot line chart
#----------------------------------
else:  
    print('\nPlotting with Matplotlib')
    # Alternatively, you can do the plot using Matplotlib or 
    # any other Python plotting library
    plt.plot(temp_table)
    plt.xlabel("Day")
    plt.ylabel("Temperature(Celsius)")
    plt.title("Daily Temperature for each Student")
    plt.legend(list(temp_table), loc="upper center", title="Name")
    plt.axhline(y=38.0, color="red", linestyle="dashed")
    plt.axhline(y=37.0, color="green", linestyle="dashed")
    plt.show()

