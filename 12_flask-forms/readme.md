When the form button is pressed, authenicate method runs. The request in authenticate method is a GET request because it uses the args method. In the login.html file, if you add a method="" field to the <form> tag, replacing "" with POST will cause an error because of bad-request. However, if method="POST" and you replace request.args (in authenticate method) with request.form, there will be no error. 

Question: It doesn't seem to matter what type of request authenicate is. Why? Does <form> do a POST request to matter what the action parameter is? 

Response: ~~The action parameter is what happens after the form is submitted, therefore, the POST request has already been completed. Therefore the request type of authenticate does not matter. It seems like submitting the form tag does send a POST request, however, the route switches to /auth so you can't really print out the POST request out without switching up the action parameter in the form tag~~. 

Response_response: Actually, it seems as if I have no idea what I'm taking about. A form can be both GET or POST, GET and POST requests both have ways of accessing data. GET retrieves data, while POST modifies it. 