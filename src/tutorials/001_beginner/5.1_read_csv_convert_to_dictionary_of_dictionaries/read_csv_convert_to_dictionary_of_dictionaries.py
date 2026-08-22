# read_csv_convert_to_dictionary_of_dictionaries.py

import pandas as pd

df = pd.read_csv('data.csv')

# Set 'name' as the key and convert to Dict of Dicts
data_obj = df.set_index('Name').to_dict(orient='index')

print(data_obj)

####

'''
{'Tabitha': {'Score': 98}, 'Jane': {'Score': 95}, 'Jennifer': {'Score': 90}, 'Alison, Martin': {'Score': 89}}
'''

'''
{
    'Tabitha':
    {
        'Score': 98
    },

    'Jane':
    {
        'Score': 95
    },

    'Jennifer':
    {
        'Score': 90
    },

    'Alison, Martin':
    {
        'Score': 89
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

