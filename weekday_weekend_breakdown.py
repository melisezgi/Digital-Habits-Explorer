#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:44:15 2025

@author: melisaydin
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load the Data
file_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/data/screen_time_data.xlsx'

# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at {file_path} does not exist.")

# Load the dataset
data = pd.read_excel(file_path)

# Step 2: Group Data by Weekday/Weekend and Category
category_daytype = data.groupby(['Weekday/Weekend', 'Category'])['Screen Time (In Minutes)'].mean().unstack()

# Step 3: Plot the Breakdown
plt.figure(figsize=(12, 6))
category_daytype.plot(kind='bar', stacked=True, colormap='viridis', ax=plt.gca())

# Add plot details
plt.title('Average Screen Time by Category and Day Type')
plt.xlabel('Day Type')
plt.ylabel('Average Screen Time (Minutes)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Step 4: Save the Plot
output_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/visuals/category_weekday_weekend_breakdown.png'

# Ensure the visuals folder exists
visuals_dir = os.path.dirname(output_path)
os.makedirs(visuals_dir, exist_ok=True)

plt.savefig(output_path)
plt.show()

print(f"Category weekday/weekend breakdown plot saved successfully to: {output_path}")
