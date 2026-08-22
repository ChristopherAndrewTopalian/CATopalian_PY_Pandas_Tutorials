# read_csv_convert_to_list_of_dictionaries_export_json.py

import pandas as pd
import json

# Load the CSV and create the array of objects
df = pd.read_csv('data.csv')
data_array = df.to_dict(orient='records')

# Write the array to a JSON file
with open('exported_data.json', 'w') as json_file:
    # dump() takes two main things: the data, and the file to write it into
    json.dump(data_array, json_file, indent=4)

print("Successfully exported to JSON!")

####

'''
[
    {
        "Name": "Tabitha",
        "Score": 98
    },
    {
        "Name": "Jane",
        "Score": 95
    },
    {
        "Name": "Jennifer",
        "Score": 90
    },
    {
        "Name": "Alison, Martin",
        "Score": 89
    }
]
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

