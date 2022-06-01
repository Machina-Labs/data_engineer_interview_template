This challenge is a 2 part:

Using RapidAPI.com, write a python script that fetches JSON data from `https://world-population.p.rapidapi.com/population`. An API key may be required, feel free to sign up as it's free or request an key from us. 

Please ensure your script completes the following:

1) Fetches JSON Data from `https://world-population.p.rapidapi.com/population`

2) Loop over all countries and get population

3) Grab the average population across all countries sorted by Population size.

Use the starter script below to complete this assignment.

Here is a starter script so your setup to talk to RapidAPI:

```python
from tqdm import tqdm

# rename some countries to later match the country names from RapidAPI
df_happiness = df_happiness.apply(lambda x: x.replace("Congo (Kinshasa)", "DR Congo"))
df_happiness = df_happiness.apply(lambda x: x.replace("Congo (Brazzaville)", "Congo"))
df_happiness = df_happiness.apply(lambda x: x.replace("Ivory Coast", "Côte d'Ivoire"))

# create URL and headers for API call
url = "https://world-population.p.rapidapi.com/population"

# the headers can be found when logging in to your RapidAPI account and opening the link above
headers = {
    'x-rapidapi-host': "world-population.p.rapidapi.com",
    'x-rapidapi-key': "***************************"
}

# add population column first by setting all values to NaN
df_happiness["Population"] = np.nan
```

2nd Assignment:

Using the dataset `https://www.worlddata.info/average-age.php`, please write a script in Python to solve the following questions.

1) Pull the average age per country data from the worlddata website and store it in a Pandas data frame.

2) Add the data into a jupyter notebook and graph out the data you averaged in the 1st question. 

3) Add a Transform section of your script (ETL), this transform should add a column to calulate the GDP of each country, This can be computed by multiplying the columns “GDP per capita” and “Population”.

4) The `Population under 20 years old` column is a string, convert it to a float. Show how you would do this in your script by adding a comment.

4) You may notice some data missing in the dataset, please call it out if you find it - Extra Credit