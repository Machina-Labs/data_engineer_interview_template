In this challenge, there are two parts, we will be having you write a few queries reading data from a SQL table. In the Challeges folder, you will find a directory called `sql_data`. This holds a file with a sample SQL Data. 

If you wish, you can load the `main.sql` into your own local MySQL or SQLite Database. The data you will be querying is `data.txt`. 

Note: There is a section at the bottom of `main.sql` where you can write your queries. 

1) Write a Query to retrieve the top 5 employees based on sorted hire date. Earlist date being on top in the sort. 

2) Write a Query to retrieve employees based on Highest Salary. 

3) Write a query to list the number of jobs available.

4) Write a query to get the maximum salary of an employee working as a Programmer.

5) Write a query to get the average salary and number of employees working the department 90.

## Part 2

Please add comments to each part of the script below on the function that each part does. 

```
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import numpy as np

# Add Comment here
html_data = requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report")

# Add Comment here
print(html_data.status_code)

# Add Comment here
soup = BeautifulSoup(html_data.text, "html.parser")

# Add Comment here
tables = soup.find_all('table',{'class':"wikitable"})

# Add Comment here
table = tables[0]

# Add Comment here
data = pd.read_html(str(table))
df_happiness = pd.DataFrame(data[0])
```