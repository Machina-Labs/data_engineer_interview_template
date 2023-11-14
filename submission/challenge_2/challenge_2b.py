#The second part of challenge 2, commenting on the code below:

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import numpy as np

# this is a one-time request to pull the HTML data from the wikipedia article "World Happiness Report"
html_data = requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report")

# print the HTTP status code from the API request, expect 200 for a successful get request
print(html_data.status_code)

# web page scraping tool beautiful soup is being used to parse raw HTML and convert it into pythonic terminology
soup = BeautifulSoup(html_data.text, "html.parser")

# with the HTML now exposed to the beautiful soup python library, any tables it was able to parse can now be easily identified and assigned an accessible variable called tables
tables = soup.find_all('table',{'class':"wikitable"})

# This selects the first table in tables
table = tables[0]

#These two lines of code are used for converting the raw HTML string previously identified as a table into a dataframe, allowing it to be more easily manipulated and analyzed
data = pd.read_html(str(table))
df_happiness = pd.DataFrame(data[0])