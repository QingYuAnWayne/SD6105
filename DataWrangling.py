import matplotlib.pyplot as plt
import pandas as pd
import scipy

Temp1 = pd.read_csv('./Temp_Week_1.csv')  # change to your directory
Temp2 = pd.read_csv('./Temp_Week_2.csv')
print('\nTable read in\n',Temp1,'\n')
print('\nTable read in\n',Temp2,'\n')

# Fill the missing value
# Temp1 = Temp1.fillna(Temp1.mean())
# Interpolation
Temp1['Temp'] = Temp1['Temp'].interpolate()

# concat
Temp = pd.concat([Temp1, Temp2], ignore_index=True)

# Pivot
temp_table = Temp.pivot(
    index="Day", columns="Week", values="Temp"
)
new_index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp_table = temp_table.reindex(new_index)

# Plot Line Graph1
temp_table.plot()
plt.xlabel("Day of Week")
plt.ylabel("Temperature(Celsius)")
plt.title("Average Daily Temperature Changes")
plt.show()

# Plot Line Graph2
Temp['Day'] = Temp['Day'].str.cat(Temp['Week'])
Temp = Temp.loc[:, ['Day', 'Temp']]
Temp.plot(x='Day')
plt.xlabel("Day of Week")
plt.ylabel("Temperature(Celsius)")
plt.title("Average Daily Temperature over 2 Weeks")
plt.show()



