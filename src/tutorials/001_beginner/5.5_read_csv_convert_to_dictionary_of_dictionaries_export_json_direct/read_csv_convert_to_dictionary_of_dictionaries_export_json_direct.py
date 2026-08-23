# read_csv_convert_to_dictionary_of_dictionaries_export_json_direct.py

import pandas as pd

# Load the CSV
df = pd.read_csv('data.csv')

# Set index to 'name' and export directly
df.set_index('Name').to_json('exported_dict_data.json', orient='index', indent=4)

print("Successfully exported Dictionary of Dictionaries to JSON!")

####

'''
{
    "Tabitha":{
        "Score":98
    },
    "Jane":{
        "Score":95
    },
    "Jennifer":{
        "Score":90
    },
    "Alison, Martin":{
        "Score":89
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

