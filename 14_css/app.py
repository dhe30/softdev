'''<!-- 
Green Monkeys; Daniel He, Faiyaz Rafee
SoftDev
K12 -- Flask forms
2022-10-17
time spent: 1 hr
 -->'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def serve():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()