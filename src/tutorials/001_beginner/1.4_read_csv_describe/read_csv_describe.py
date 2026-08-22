# read_csv_describe.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData.to_string())

print('-------------------------------')

# Prints mathematical stats (average, min, max) for all number columns
print(theData.describe())

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
           Score
count   4.000000
mean   93.000000
std     4.242641
min    89.000000
25%    89.750000
50%    92.500000
75%    95.750000
max    98.000000
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

