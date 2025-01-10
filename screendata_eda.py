#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:32:47 2025

@author: melisaydin
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Define Absolute Paths
file_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/data/screen_time_data.xlsx'
visuals_dir = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/visuals'

# Ensure the visuals folder exists
os.makedirs(visuals_dir, exist_ok=True)

# Step 2: Load the Data
data = pd.read_excel(file_path)
print("Data loaded successfully. Here's a preview:")
print(data.head())

# Step 3: Daily Screen Time Trend
daily_screen_time = data.groupby('Date')['Screen Time (In Minutes)'].sum()

# Plot daily screen time trend
plt.figure(figsize=(10, 6))
plt.plot(daily_screen_time.index, daily_screen_time.values, marker='o', linestyle='-', color='blue')
plt.title("Daily Screen Time Trend")
plt.xlabel("Date")
plt.ylabel("Screen Time (Minutes)")
plt.grid()
output_path = os.path.join(visuals_dir, "daily_screen_time_trend.png")
plt.savefig(output_path)
plt.show()
print(f"Daily screen time trend saved to: {output_path}")

# Step 4: Category-wise Screen Time Analysis
category_screen_time = data.groupby('Category')['Screen Time (In Minutes)'].sum()

plt.figure(figsize=(10, 6))
category_screen_time.sort_values(ascending=False).plot(kind='bar', color='orange')
plt.title("Total Screen Time by Category")
plt.xlabel("Category")
plt.ylabel("Screen Time (Minutes)")
plt.xticks(rotation=45)
output_path = os.path.join(visuals_dir, "screen_time_by_category.png")
plt.savefig(output_path)
plt.show()
print(f"Category-wise screen time saved to: {output_path}")
