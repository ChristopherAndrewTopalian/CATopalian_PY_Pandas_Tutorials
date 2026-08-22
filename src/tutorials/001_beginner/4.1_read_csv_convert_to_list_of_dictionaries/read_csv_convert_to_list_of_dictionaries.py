# read_csv_convert_to_list_of_dictionaries.py

import pandas as pd

# Load the CSV
df = pd.read_csv('data.csv')

# Convert to a List of Dictionaries (Array of Objects)
data_array = df.to_dict(orient='records')

print(data_array)

'''
[{'Name': 'Tabitha', 'Score': 98}, {'Name': 'Jane', 'Score': 95}, {'Name': 'Jennifer', 'Score': 90}, {'Name': 'Alison, Martin', 'Score': 89}]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

