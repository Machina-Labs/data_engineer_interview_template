'''
1) get input
2) validate and convert input
3) transform object
4) return to user

'''


import json
import sys


def recombinator(conversion):
    try:
        #this loads the JSON input as a python dict, and fails if the input does not convert
        usr_input = json.loads(conversion)
    except:
        #this is excpetion is for invalid inputs
        print('Error: Not a valid JSON input')
    
    #initialize the reformatted dict
    redict = dict()

    #this was added to give a descriptive error for when a user passes an already processed file or otherwise non-nested list to the function
    if not isinstance(usr_input, list):
        raise ValueError('cannot recombinate non-list')

    #this loop determines which logical path to follow for reformatting by checking the data type of the first sub list
    if isinstance(usr_input[0], dict):
        #due to the sparse nature of the list of objects input type, the first loop logs all possible keys and initialize their values as null
        for i in range(len(usr_input)): 
            for key in usr_input[i].keys():
                if redict.get(key) is not None:
                    continue
                else:
                    redict.update({key:[None for i in range(len(usr_input))]})
        #the second loop overwrites null values with real values as they appear
        for i in range(len(usr_input)):
            for key, value in usr_input[i].items():
                redict[key][i] = value
    
    #because the second input type contains all possible keys in the first sub list, the key and values can be assigned in the same line with the use of list comprehension 
    elif isinstance(usr_input[0], list):
        for i in range(len(usr_input[0])):
            redict.update({usr_input[0][i]:[usr_input[j][i] for j in range(1,len(usr_input))]})        
    
    #this exception is raised when a valid JSON input is given, but does not adhere to the terms laid out in the problem statment
    else:
        raise ValueError('Not an accepted input type')

    #converting back to JSON and printing the output
    print(json.dumps(redict))

    return


#initializer to enable calling functions and passing args from the command line
if __name__ == "__main__":
    globals()[sys.argv[1]](sys.argv[2])