# Digital-Habits-Explorer
This project analyzes personal screen time data to uncover insights into daily smartphone usage patterns.
# Screen Time Analysis

## Introduction
This project explores screen time habits using personal data collected over a month. 
The analysis includes daily trends, category-wise usage, and a comparison between weekdays and weekends.
In addition, statistical hypothesis testing was performed to determine significant differences in screen time patterns between weekdays and weekdays.

## Dataset Description
The data was collected from my smartphone's built-in screen time tracker. It includes daily usage data categorized by apps, total screen time, and usage times across different days.

## Project Plan
1. **Exploratory Data Analysis (EDA)**:
- Summarize the total screen time and app usage across the week.
- Identify patterns, such as peak usage times and differences between app categories.
- Compare weekday and weekend usage to spot behavioral shifts.
2. **Visualization**:
- Create charts for screen time distribution and app usage trends.
3. **Findings**:
- Summarize insights, such as the most-used apps or categories and areas for improvement.
4. **Future Work**:
- Explore predictive modeling to estimate future screen time trends.
- Develop strategies to improve productivity and reduce distractions.

### Methods
1. Data Analysis:
   - Analyzed trends in daily screen time using line plots.
   - Categorized and compared screen time across different app categories.
2. Statistical Hypothesis Testing:
   - Conducted a t-test to determine if there is a significant difference in screen time between weekdays and weekends.
3. Visualizations:
   - Used Matplotlib and Seaborn for creating visuals to better understand the data.


## Deliverables
The repository will include:

 - Analysis Scripts:
Python scripts for data cleaning, EDA, and visualization.
 - Visualizations:
The following visualizations were generated to explore the data:
1. Daily Screen Time Trend: This line chart shows how screen time varies across the month. (daily_screen_time_trend.png)
2. Screen Time by Category: A bar chart illustrating the total screen time spent on each category. (screen_time_by_category.png)
3. Weekday vs Weekend Comparison: A boxplot comparing screen time distributions for weekdays and weekends. (screen_time_boxplot.png)


 - README.md:
A detailed explanation of the project, including its goals, methodology, and findings.
 - GitHub Repository:
All project materials, excluding raw data for privacy.

## Timeline
- Project repository setup: Completed by Nov 30.
- Exploratory Data Analysis and Findings: January 2024.
- Final analysis and findings: To be submitted by Jan 10.

## Limitations
This analysis is based on personal data, so insights may not generalize to others. The dataset may also have incomplete records due to phone inactivity on some days.

## FINDINGS
Screen time is significantly higher on weekends compared to weekdays (P-value < 0.05).
Social media apps account for the largest portion of total screen time.
Screen time patterns show consistency on weekdays, with noticeable spikes on weekends.

## Future Work
Incorporate data from additional months for a more comprehensive analysis.
Explore correlations between screen time and productivity metrics.
Add machine learning models to predict screen time based on historical dat


