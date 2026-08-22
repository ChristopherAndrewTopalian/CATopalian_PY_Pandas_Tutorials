# read_csv_convert_to_dictionary_of_dictionaries_filter_by_name.py

import pandas as pd

# Load the data
df = pd.read_csv('data.csv')

# Set 'Name' as the index, then convert to a Dictionary of Dictionaries
data_dict = df.set_index('Name').to_dict(orient='index')

# Show just the names
# In a Dictionary of Dictionaries, the names are now the master keys
print("List of Names (Keys)")
for name in data_dict.keys():
    print(name)

print("\nInstant Data Lookup")

print(f"Tabitha's data: {data_dict['Tabitha']}")

####

'''
List of Names (Keys)
Tabitha
Jane
Jennifer
Alison, Martin

Instant Data Lookup
Tabitha's data: {'Score': 98}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

