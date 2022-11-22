# Daniel He, Samson Wu
# SoftDev
# K20 -- restapi
# 2022-11-21
# time spent: 1 hour

## QCC:
* Sometimes API response times take a while. How does flask handle non-trivial response times? Does the html not render until the request gets a response? Does it dynamically render elements when they are recieved? Do you just get a white screen?  

## DISCO:
* You can turn your request with url into a json dict using request.json()
* The request object of response.get(url, params) evaluates to False if the request HTTP code is an error (5XX, 4XX)
* The params field passed into the get function is a dictionary specifying the parameters that go along with the url (i.e. API key)
* Accessing json objects is the same as python dictionaries 