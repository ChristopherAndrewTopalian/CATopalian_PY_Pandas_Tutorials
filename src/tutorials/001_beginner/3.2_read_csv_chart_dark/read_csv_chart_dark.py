# read_csv_chart_dark.py

import pandas as pd
import matplotlib.pyplot as plt

# Turn on the global dark theme!
plt.style.use('dark_background')

# Load your data
theData = pd.read_csv('data.csv')

print(theData.to_string())

# Plot the chart and force the bars to be neon cyan
theData.plot(kind='bar', x='Month', y='Sales', color='#00FFFF')

# Display it
plt.show()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

