"""
TEAM FLASKERS - Harry ZHu, Kevin Wang, Daniel He
SoftDev
k10 -- Using a template
2022-10-07
time spent: 0.5 hrs

"""
'''
0. Prediction: only "/" route works, but the other one will produce an error message
   Actual: same as prediction 
1. It is the same as the string in .route(); it is placed at the end of the domain 
2. Prediction: the first argument is the template name, the rest of the arguments can be anything you want 

'''
from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'new.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

if __name__ == "__main__":
    app.debug = True
    app.run()
