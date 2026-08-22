# read_csv_filter_by_year.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData.to_string())

print('-------------------------------')

# Show only the rows where the 'Year' column equals 2026
recent_data = theData[theData['Year'] == 2026]

print(recent_data)

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
      Name  Score  Year
0  Tabitha  98  2026
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

