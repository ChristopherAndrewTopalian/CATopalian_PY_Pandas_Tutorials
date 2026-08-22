# read_csv_convert_to_dictionary_of_dictionaries_export_json.py

import pandas as pd
import json

# Load the CSV
df = pd.read_csv('data.csv')

# Set 'name' as the index and convert to a Dictionary of Dictionaries
data_dict = df.set_index('Name').to_dict(orient='index')

# Write the dictionary to a JSON file
with open('exported_dict_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Successfully exported Dictionary of Dictionaries to JSON!")

####

'''
{
    "Tabitha": {
        "Score": 98
    },
    "Jane": {
        "Score": 95
    },
    "Jennifer": {
        "Score": 90
    },
    "Alison, Martin": {
        "Score": 89
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

