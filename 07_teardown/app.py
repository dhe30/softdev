'''
Selena Ho, Shafiul Haque, Daniel He
SoftDev
K07 -- Starting Flask
2022-10-03
time spent: 0.5
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. Similar to Java syntax for objects
1. It's present in links to websites for example, like github.com/stuy-softdev
2. it will print in the URL (after running: it actually prints in the shell and prints __main__ but only after pressing the clickable link)
3. the name of the app
4. it'll return in the shell if you call hello_world() (after running: it appears in the website that is linked in the shell)
5. Java - it's like calling methods on objects
...
INVESTIGATIVE APPROACH:
We tried to figure out on our own without running the code first to see what might appear. Then, once we finished going through each question, we ran the code and pressed the link that appeared to see what would happen.
'''