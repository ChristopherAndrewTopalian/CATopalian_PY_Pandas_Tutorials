# read_csv_make_chart.py

import pandas as pd
import matplotlib.pyplot as plt

theData = pd.read_csv('data.csv')

print(theData.to_string())

# Create a bar chart. X-axis is Month, Y-axis is Sales.
theData.plot(kind='bar', x='Month', y='Sales')

# Physically pop open the window to show the chart
plt.show()

####

'''
             Name  Score  Year  Team                  Job    Month  Sales
0  Tabitha  98  2026  Red  Engineer  January  4000
1  Jane  95  2025  Blue  Computer Scientist  August  5000
2  Jennifer  90  2025  Red  AI Specialist  June  1000
3  Alison, Martin  89  2024  Blue  Robotics Technician  March  500
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

