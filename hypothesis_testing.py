#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:36:30 2025

@author: melisaydin
"""

import pandas as pd
from scipy.stats import ttest_ind

# Step 1: Load the Data
file_path = '/Users/melisaydin/Desktop/DigitalHabitsExplorer/data/screen_time_data.xlsx'
data = pd.read_excel(file_path)

# Step 2: Separate Weekdays and Weekends
weekdays = data[data['Weekday/Weekend'] == 'Weekday']['Screen Time (In Minutes)']
weekends = data[data['Weekday/Weekend'] == 'Weekend']['Screen Time (In Minutes)']

# Step 3: Perform the T-Test
t_stat, p_value = ttest_ind(weekdays, weekends)

# Step 4: Print the Results
print("Hypothesis Testing Results:")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")

# Step 5: Check Significance
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Result: There is a significant difference in screen time between weekdays and weekends.")
else:
    print("Result: There is no significant difference in screen time between weekdays and weekends.")
