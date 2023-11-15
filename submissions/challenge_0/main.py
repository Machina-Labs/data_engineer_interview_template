'''
Hello! This is Gisselle, welcome to my code!
'''

import json
import pandas as pd


# This function determines what format the json string is in and how to parse the format 
def json_determine(test_case):
    # a map will always have curly bracket 
    if '{' in test_case.split(' '):
        parse_map(test_case)
    # where as anything without a curly bracket is a double list
    else:
        parse_double_list(test_case)


# function to parse json strings that are in the form of a double list. Takes the jsoon string as argument "test"
def parse_double_list(test):
    # reading the json string as list of tuples
    test = json.loads(test)
    # turning the list of rows into a pandas dataframe to manipulate.
    # setting the first row as the colmon names and the rest of the items as rows in the table,
    # while also setting all NaN nalues as "null"
    df = pd.DataFrame(test[1:], 
       columns=test[0]).fillna("null")
    #getting a list of all the column names
    cols = df.columns.to_list()

    print('THE RESULTS: \n')
    #intallizing list that will store all the columns as separate lists
    values = []
    #iterating every column in the dataframe to store the result list
    for c in cols:
        col = df[c].to_list()

        values.append(col)
    #using the names of columns as the keys and the column contents as values to create a dictionary format
    result = dict(zip(cols, values))
    #returning the end result
    print(result)


def parse_map(test):
    # turning the map into a pandas dataframe to manipulate.
    # Setting all NaN values in the dataframe as "null'
    test = json.loads(test)
    df = pd.json_normalize(test).fillna("null")
    #getting a list of all the column names
    cols = df.columns.to_list()

    print('THE RESULTS: \n')
    #intallizing list that will store all the columns as separate lists
    values = []
    #iterating every column in the dataframe to store the result list
    for c in cols:
        col = df[c].to_list()

        values.append(col)
    #using the names of columns as the keys and the column contents as values to create a dictionary format
    result =  dict(zip(cols, values))
    #returning the end result
    print(result)

#requesting the json input from the user in cmd prompt
input_json = input("Please enter your json string")

#taking the user's response and running it in the code
json_determine(input_json)
