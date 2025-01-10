#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:43:32 2025

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

# Step 2: Group Data by Date and Category
category_trends = data.groupby(['Date', 'Category'])['Screen Time (In Minutes)'].sum().unstack()

# Step 3: Plot the Trends for Each Category
plt.figure(figsize=(12, 6))
category_trends.plot(ax=plt.gca(), linewidth=2)

# Add plot details
plt.title('Screen Time Trends by Category Over Time')
plt.xlabel('Date')
plt.ylabel('Screen Time (Minutes)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout()

# Step 4: Save the Plot
output_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/visuals/category_trends_over_time.png'

# Ensure the visuals folder exists
visuals_dir = os.path.dirname(output_path)
os.makedirs(visuals_dir, exist_ok=True)

plt.savefig(output_path)
plt.show()

print(f"Category trends plot saved successfully to: {output_path}")
