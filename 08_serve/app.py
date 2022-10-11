"""
TEAM FLASKERS - Harry ZHu, Kevin Wang, Daniel He
SoftDev
k05 -- Using a flask app to return a random occupation on a website
2022-10-07
time spent: 1.5 hrs

Disco:
* f strings to insert the result of python code into a string
* how to use modules (using github guide)
* flask must have one return value so use a string with HTML to parse multiple outputs


QCC:
* __x__ is some special syntax in markdown
* how is css handled in flask?
* why can't multiple values be returned in one function in flask?


HOW THIS SCRIPT WORKS:
1. Imports flask and occupation, where occupation.py represents the functions for lab 07
2. Creates a flask app
3. In the global scope, parses out the list of occupations from the dictionary of occupations to percentages and adds it to a string, string_of_occupations
4. In the home route of flask, define the function random_occupation, which returns a string consisting of the TNPG + roster + results of generating a random occupation + list of occupations

"""

from flask import Flask
import occupation #this is a copy of 06_py_csv

app = Flask(__name__) #create instance of class Flask

string_of_occupations = ""
occupation_to_percent, total_percent = occupation.csv_to_dictionary() #move outside of the function because it is static
occupations = list(occupation_to_percent.keys())
for oc in occupations:
    string_of_occupations += oc + "</br>"


@app.route("/")       #assign fxn to route
def random_occupation():
    return_value = "TEAM FLASKERS - Harry ZHu, Kevin Wang, Daniel He </br>"

    return_value += f"<h1> {occupation.get_random_occupation()} </h1></br>"

    return return_value + string_of_occupations
    

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

