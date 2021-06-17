# Introduction to Flask and Jinja

### Learning Objectives

#### General

**What is a Web Framework**

Web framekwork is a software framework designed to support the development of web applications.  Web frameworks are used to support web services, web resources, and web API's.  Such frameworks provice a standard way to build and deploy web applications on the World Wide Web. Web frameworks seek to automate the overhead associated with common activities performed. 

**How to build a web framework with Flask**

	* Flask is a web framekwork written in python
	* Flask is a micro framework which does not require any additional tools or libraries
	* Flask has a "component" called **Jinja** which is a template engine.

Flask can be sued with Puthon to build a backen for interactive web applications.  Flask allows you to seamlessly connect a database to a web application. The application will be able to react to dynamic user input.  Instead of a abstraction layer for database support, Flask supports extensions for such capabilities.

**How do you define routes in Flask?**

	* Flask uses the **route()** decorateor to declare routes.
	* **route()** binds a function to a URL

**What is a "route" in Flask?**

A decorator that is used to register a view function for a give URL rule.  

	* **rule** - the URL rule as a _string_
	* **endpoint** - endpoint for registered URL rule.
	* **options** - options to be forwarded to the underlying rule object.
```
route(rule, **options)
```

**How to handle variables in a route**

You can add variable sections to a URL by marking sections with **<variable_name>**.  The function then recieves the variable as a keyword argument.

**What is a template?**

	* The result of a template is a full HTML page sent to the client.
	* The process is called _rendering the template_, because rendering results in whatever the client sees.

### Setting up a Flask application:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World!'

if __name__ == '__main__':
   app.run()
```

### Routing

Flask uses the route() decorator to declare routes. The first example below uses app.route("/") to declare a route for “/” that resolves to hello(), but you can use any path, or even accept variables in your routes:

```

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/my/secret/page")
def secret():
    return "Shh!"

@app.route("/user/<username>")
def user_page(username):
    return f"Welcome, {username}!"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for post # {post_id}"
```

Flask uses the route() decorator to declare routes. For example, the above code uses app.route("/") to declare a route for “/” that resolves to hello(), but you can use any path, or even accept variables in your routes:


### Variable Rules

You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

```
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```

#### Converter Types for Variables
	* string - default, accepts any text without a slash
	* int - accepts positive integers
	* float - accepts positive floating point values
	* path - like string but also accepts slashes
	* uuid - accepts UUID strings
	 
### Sending data to Flask template (Jinja)
Flask sends form data to template Flask to send form data to the template we have seen that http method can be specified in the URL rule.Form data received by the trigger function can be collected in the form of a dictionary object and forwarded to the template to render it on the corresponding web page.
