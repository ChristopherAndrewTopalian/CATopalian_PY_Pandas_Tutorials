# read_csv_convert_to_dictionary_of_dictionaries_show_names.py

import pandas as pd

df = pd.read_csv('data.csv')
data_dict = df.set_index('Name').to_dict(orient='index')

# loop through the keys
for name in data_dict:
    print(name)

####

'''
Tabitha
Jane
Jennifer
Alison, Martin
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

