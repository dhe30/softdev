#v0

Notable
*flask is imported from flask - why not just import Flask? what is the difference
*what is __name__?
*is the function hello_world() automatically run without explicitly doing hello_world()
*CTRL+C to close the website
*what is a production WSGI server?
*what is debug mode and how do you turn it on?
*what does 200 represent?

Expected Behavior
*print should print something to the terminal
*return should be the output on the website

Actual Behavior
*__main__ is printed to the terminal
* No hablo queso! is displayed on the website

#v1

Notable
*app = Flask(__name__) looks like making an instance of a Java class -> Flask is a class?
*hello_world is bound to the route of "/" so it's automatically ran when "/" is requested

Expected Behavior
same as v0 except no printing

Actual Behavior
same as v0 except no printing

v2

Notable
*same as v0 and v1
*__name__ is __main__

Expected Behavior
*"about to print __name__... \n __main__" to the console
* No hablo queso! is displayed on the website

Actual Behavior
* same as expected

v3
Notable
*app.debug is set to True, whereas it was false before
*syntax is similar to setting java field in a class for app.debug -> confirms app is an instance of Flask
*when the code changes, the website is refreshed with the new code now
Expected Behavior
* expect "Debug mode: on" to be printed to the terminal
* same other expected behavior as v2 in addition to debug mode

Actual Behavior
* three new lines:
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 910-861-683
* when an error is made like 5/0 in hello_world, an UI shows up on the website that shows the error, in addition to the error message being printed to the console, but the code doesn't stop. "The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error. " is shown on the website


v4
Notable
"if __name__ == "__main__":" line - why is this necessary? is it necessary?

Expected Behavior
*the same as v3 because __name__ should be equal to "__main__"

Actual Behavior
*same as expected