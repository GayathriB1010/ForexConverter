# ForexConverter
### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is a scripting language used for developing both desktop and web applications. Javascript is a client side scripting language.Python is a class based inheritance model. Javascript is a prototype based inheritance model.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

Using get()
For example :  d= {"a": 1, "b": 2} . d.get('c','not found').  if key is present, value associated with it is printed or not found is printed. setdefault(key,value). This works the same way as get.but the difference is each time 
a key is absent, a new key is created with the value associated with the key.

- What is a unit test?

Unit testing involves the testing of each unit or an individual component of the software application. A unit is a single testable part of a software system and tested during development phase of the application software.

- What is an integration test?

Integration testing is defined as a type of testing where software modules are integrated logically and tested as a group. 

- What is the role of web application framework, like Flask?
 A Web-Application Framework or Web Framework is the collection of modules and libraries that helps the developer to write applications without writing the low-level codes such as protocols, thread management, etc. Flask is based on WSGI(Web Server Gateway Interface) toolkit and Jinja2 template engine.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

You can generally use query string parameters if you are describing the object you are on vs using the route for the object itself. For example, in the above case I would use /foods/pretzel and then use a query string parameter if I am decribing the pretzel such as /foods/pretzel?type=salty or /foods/pretzel?type=sugar.

- How do you collect data from a URL placeholder parameter using Flask?


- How do you collect data from the query string using Flask?

using request.args.get()

- How do you collect data from the body of the request using Flask?
request.form.get()

- What is a cookie and what kinds of things are they commonly used for?
Cookies are name/string-value pair stored by the client (browser).

The server tells client to store these.

The client sends cookies to the server with each request.

- What is the session object in Flask?

Contain info for the current browser
Preserve type (lists stay lists, etc)
Are “signed”, so users can’t modify data

- What does Flask's `jsonify()` do?
