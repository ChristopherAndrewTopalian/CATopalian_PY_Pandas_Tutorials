# read_csv_info.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData.to_string())

print('-------------------------------')

# Prints all column names, how many rows exist, and if any data is missing
print(theData.info())

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    4 non-null      object
 1   Score   4 non-null      int64
dtypes: int64(1), object(1)
memory usage: 196.0+ bytes
None
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

