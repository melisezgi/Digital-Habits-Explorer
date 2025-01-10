#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:54:05 2025

@author: melisaydin
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Load the Data
file_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/data/screen_time_data.xlsx'

# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at {file_path} does not exist.")

# Load the dataset
data = pd.read_excel(file_path)

# Preview the dataset (optional)
print("First 5 rows of the dataset:")
print(data.head())

# Step 2: Add 'Day Type' Column
# Ensure 'Weekday/Weekend' column exists
if 'Weekday/Weekend' not in data.columns:
    raise ValueError("'Weekday/Weekend' column is missing in the dataset.")

# Create a 'Day Type' column for easier plotting
data['Day Type'] = data['Weekday/Weekend']

# Step 3: Generate the Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Day Type', y='Screen Time (In Minutes)', data=data, palette='pastel')
plt.title('Screen Time Distribution: Weekdays vs Weekends')
plt.xlabel('Day Type')
plt.ylabel('Screen Time (Minutes)')
plt.tight_layout()

# Step 4: Save the Plot
output_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/visuals/screen_time_boxplot.png'

# Ensure the visuals folder exists
visuals_dir = os.path.dirname(output_path)
os.makedirs(visuals_dir, exist_ok=True)

plt.savefig(output_path)
plt.show()

print(f"Boxplot saved successfully to: {output_path}")
