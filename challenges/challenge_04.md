In this challenge, you will develop a script, feel free to add it to this repository in your Pull Request or use a tool like PythonAnywhere.com or Play.golang.org.

Your script should retrieve a file or JSON from a public source on a daily basis, so please include a description on how you would achieve that. The script should then update a persistance data store my MySQL. 

In this example, use the freely available dataset from [Google's Health System](https://health.google.com/covid-19/open-data/), which contains open data for COVID counts related to hospitalizations in CA. 

Here are some details, you should follow:

1) Review and understand hospitalization data available at the above-mentioned link.

2) Generate a SQL script to create a MySQL database to hold required information.

3) Create a local MySQL database.

4) Create a script that can be run as a Daemon to do the following on a daily basis.

5) If your famaliar with Docker, write a `Dockerfile` that containerizes your script. 

With your newly created MySQL Database, fetch the latest CSV or JSON from [HERE](https://storage.googleapis.com/covid19-open-data/v3/hospitalizations.csv).

Pull the updated data on hospitalizations in CA and write it to a MySQL Table in your database. 

Please show the SQL code and Query you perform to update the data in MySQL.

If your unable to run MySQL locally on your system, feel free to use [SQLITE](https://www.sqlite.org/index.html)