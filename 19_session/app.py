'''
Green Monkeys; Daniel He, Faiyaz Rafee
SoftDev
K19 -- Cookies
2022-11-3
time spent:
'''
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session, redirect

app = Flask(__name__)    #create Flask object
app.secret_key = b"hehe" #secret key needed to create a session 
username = "octopus"
password = "avacado"

@app.route("/response", methods=["GET","POST"])
def sessionCreate():
    if request.method == 'POST': #post uses .form, html forms are default get unless specified
        if request.form["username"] == username and request.form["password"] == password:
            session["username"] = request.form["username"]
        else: 
            response = ""
            if request.form["username"] != username:
                response += "Username is incorrect!<br>" #\n does not work in html strings
            if request.form["password"] != password:
                response += "Password is incorrect!<br>"
            return render_template("login.html", error = response)
    else: 
        print("Something horribly wrong in response route, get request instead of post")
    return render_template("response.html", username = session["username"])

@app.route("/logout", methods=["GET","POST"])
def logout():
    if request.method == "GET":
        session.pop("username", None) #pop to remove things from session 
    else: 
        print("Something horribly wrong in logout route, post request instead of get")
    return redirect("/") #redirects to another route so the url makes sense and doesn't say logout 

@app.route("/")
def welcome():
    if "username" in session: 
        return render_template("response.html", username = session["username"])
    else:
        return render_template("login.html")
            
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
