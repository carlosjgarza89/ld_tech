### This script takes a user-defined Slot.ID and creates a heatmap
### That displays the Creative.ID that produces the most revenue for
### for that specific Slot.ID.

# Confirm to user that program is loading content
print('\nLoading Content... \n')

# Import Neccessary Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import processed dataframe
df = pd.read_csv('processed_data.csv')

# Request user input to define target Slot.ID
user_input = int(input('Slot.ID to analyze? '))

# Filter df by Slot.ID
filtered_df = df[df['Slot.ID']==user_input]

#Create Pivot Table
pivot_table = create_by_device = pd.pivot_table(df, values='net_revenue',
	index = ['Creative.ID'], columns=['Device'], aggfunc=np.sum, fill_value=0)

#Drop 'Other' Column
pivot_table.drop(columns=['Other'], inplace=True)

#Generate Heatmap
plt.figure(figsize=(10,10))
sns.heatmap(create_by_device, cmap='Blues')
plt.title(f'Net Revenue in USD for Slot.ID = {user_input}')
plt.show()