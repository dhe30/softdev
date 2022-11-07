Discoveries
* variables passed into templates do not need to exist for the template to render even if they are used in the template
* buttons with type "button" do not do anything and will not follow the action of the form. They should always be specified or else browsers will set a default value, which may break your code
* if B is a string with html in it and a template holds the value {{B}}, the html will not be read unless it is written as {{B | safe}}, although we don't know exactly why 
* redirect changes routes and the URL, render_template only renders the template 
* there is a input tag type called password that replaces characters with dots 
* unless specified, html forms will use GET methods 
