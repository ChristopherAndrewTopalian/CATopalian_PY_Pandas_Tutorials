# read_csv_convert_to_list_of_dictionaries_show_names.py

import pandas as pd

# Load the CSV
df = pd.read_csv('data.csv')

# Convert to a List of Dictionaries (Array of Objects)
data_array = df.to_dict(orient='records')

# Loop through all students
for person in data_array:
    print(f"{person['Name']}: {person['Score']}")

####

'''
Tabitha: 98
Jane: 95
Jennifer: 90
Alison, Martin: 89
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

