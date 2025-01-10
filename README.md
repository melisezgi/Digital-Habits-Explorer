# Digital-Habits-Explorer
This project analyzes personal screen time data to uncover insights into daily smartphone usage patterns.
# Screen Time Analysis

## Introduction
This project explores screen time habits using personal data collected over a month. 
The analysis includes daily trends, category-wise usage, and a comparison between weekdays and weekends.
In addition, statistical hypothesis testing was performed to determine significant differences in screen time patterns between weekdays and weekdays.

## Hypotheses
For the statistical analysis, the following hypotheses were tested:

Null Hypothesis (H₀):
There is no significant difference in screen time between weekdays and weekends.

Alternative Hypothesis (H₁):
There is a significant difference in screen time between weekdays and weekends.

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
1. Daily Screen Time Trend:
There is a visible fluctuation in the trend of total screen time over time.
There is a general downward trend in screen time for most days, except for spikes possibly due to specific events or weekends.

2. Category Trends Over Time:
Social Media leads the chart in screen time across almost all days, especially during weekends.
Categories like Entertainment and Shopping and Food show peaks occasionally, probably reflecting user-specific activities.
The less-used categories, such as Education and Creativity, are also relatively stable.

3. Category Screen Time Breakdown:
Social Media accounts for the majority of the total screen time, followed by Entertainment and Shopping and Food.
Productivity-related categories like Creativity and Education have very minimal contributions.

4. Weekday vs Weekend Analysis:
Screen Time is significantly higher on weekends compared to weekdays, as can be seen from both the boxplot and stacked bar chart.
While the contribution of Social Media and Entertainment-like categories is more contributive on weekends, productivity-related activities tend to remain constant between both weekends and weekdays.
Boxplot Visualization
Stacked Bar Chart

5. Key Takeaway:
Social Media is highly used during weekends, indicating that on non-working days, people are relaxing and communicating with each other.
Productive and health-related categories have remained quite constant, reflecting equal usage trends in these kinds of activities.
Peaks of entertainment might point to specific events or days on which users are into media consumption.


## Future Work
Incorporate data from additional months for a more comprehensive analysis.
Explore correlations between screen time and productivity metrics.
Add machine learning models to predict screen time based on historical dat


