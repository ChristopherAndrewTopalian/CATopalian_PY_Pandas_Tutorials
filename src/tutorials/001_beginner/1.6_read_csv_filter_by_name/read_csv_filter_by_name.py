# read_csv_filter_by_name.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData.to_string())

print('-------------------------------')

# Show only rows where the 'Name' column is 'Jane'
jane_data = theData[theData['Name'] == 'Jane']

print(jane_data)

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
   Name  Score  Year
1  Jane  95  2025
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

