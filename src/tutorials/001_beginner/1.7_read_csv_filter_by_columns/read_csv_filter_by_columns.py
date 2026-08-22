# read_csv_filter_by_columns.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData.to_string())

print('-------------------------------')

isolated_columns = theData[['Name', 'Job']]

print(isolated_columns)

####

'''
Name  Score  Year  Team  Job
0 Tabitha  98  2026   Red   Engineer
1 Jane      95  2025  Blue   Computer Scientist
2 Jennifer 90  2025  Red   AI Specialist
3  Alison, Martin  89  2024  Blue  Robotics Technician
-------------------------------
             Name               Job
0         Tabitha       Engineer
1            Jane        Computer Scientist
2        Jennifer       AI Specialist
3  Alison, Martin   Robotics Technician
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

