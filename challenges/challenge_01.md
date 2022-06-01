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