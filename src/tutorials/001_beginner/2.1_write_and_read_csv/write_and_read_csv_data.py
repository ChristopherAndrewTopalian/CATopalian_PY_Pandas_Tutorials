# write_and_read_csv_data.py

import pandas as pd
import os

def create_mission_data():
    # We create a CSV string where some data points contain commas.
    # Notice how the names and locations are wrapped in quotes.
    csv_content = """ID,Name,Last_Known_Location,Status
101,"Smith, John","Sector 4, Alpha",Rescued
102,"Doe, Jane","Sector 7, Beta",Awaiting Rescue
103,"O'Connor, Sarah","Sector 4, Alpha",Rescued
104,"Patel, Ravi","Sector 9, Delta",Awaiting Rescue"""

    # Write it to a file
    with open('rescue_manifest.csv', 'w') as file:
        file.write(csv_content)
    print("--- System: 'rescue_manifest.csv' generated on local drive. ---\n")

def main():
    # Generate the file so we have data to read
    create_mission_data()

    print("1. Loading the Rescue Manifest...")
    # This single line reads the entire file and formats it into a DataFrame
    df = pd.read_csv('rescue_manifest.csv')
    
    print("\n2. Displaying the DataFrame:")
    print(df)

    print("\n3. Isolating a Specific Column (Just the Names):")
    print(df['Name'])

if __name__ == '__main__':
    main()

####

'''
--- System: 'rescue_manifest.csv' generated on local drive. ---

1. Loading the Rescue Manifest...

2. Displaying the DataFrame:
    ID             Name Last_Known_Location           Status
0  101      Smith, John     Sector 4, Alpha          Rescued
1  102        Doe, Jane      Sector 7, Beta  Awaiting Rescue
2  103  O'Connor, Sarah     Sector 4, Alpha          Rescued
3  104      Patel, Ravi     Sector 9, Delta  Awaiting Rescue

3. Isolating a Specific Column (Just the Names):
0        Smith, John
1          Doe, Jane
2    O'Connor, Sarah
3        Patel, Ravi
Name: Name, dtype: object
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

