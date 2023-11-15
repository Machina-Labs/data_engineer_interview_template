from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import numpy as np

# Add Comment here
'''
Grabbing the hmtl information from the provided wikipedia link.
The data will be used to return a table of the Happiest countries ranked according to the report
'''
html_data = requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report")

# Add Comment here
'''
printing out the status code of the request to make sure the response was successful or if there are any errors
'''
print(html_data.status_code)

# Add Comment here
'''
the library beatifulSoup is used to scrape the information from a website. 
This function is taking in the context of the response object and parser type.   
Here, the variable soup is storing the beatifulSoup object to read through later.
'''
soup = BeautifulSoup(html_data.text, "html.parser")

# Add Comment here
'''
Using the find all functions to identify all the tables in the html based on the 'table' tag and css class 'wikitable'
to store all of the ranking tables on the wikipedia page in the list "tables
'''
tables = soup.find_all('table',{'class':"wikitable"})

# Add Comment here
'''
The variable table is storing the first element of the list of tables because it is the most recent world happiness ranking table html

'''
table = tables[0]

# Add Comment here
'''
Converting the table html to a list as data
Then taking the list and converting it as a readable pandas dataframe table of the most recent world happiness ranking list
'''
data = pd.read_html(str(table))
df_happiness = pd.DataFrame(data[0])
