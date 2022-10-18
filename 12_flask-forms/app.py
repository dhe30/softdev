'''
Green Monkeys; Daniel He, Faiyaz Rafee
SoftDev
K12 -- Flask forms
2022-10-17
time spent:
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request) #GET request
    print("***DIAG: request.args ***")
    print(request.args) #ImmutableMultiDict([])
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #BadRequestKeyError, username not defined?    
    print("***DIAG: request.headers ***")
    print(request.headers)
    if request.method == 'POST':
        print("AAAAAAAAAAAAAAA")
    else: 
        print("EEEEEEEEEEEE")
        return render_template( 'login.html' )



@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username']) #returns form input, input appears in domain address
    username = request.form.get("username")
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'response.html', user = username, request_method = request.method )


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
