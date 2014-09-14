#README.md

This is a summary document as I work through [Test Driven Development with Python](http://www.obeythetestinggoat.com/)
and hopefully learn `Django` in the process.

I'll include things like notes, sections, code snippets, and code I've worked through / modified in order to get things 
up and running.

## Chaper 2

- Use the `unittest` framework instead of simply writing functions

- The `def setUp` and `def tearDown` are special functions inside of 
  `class uittest.TestCase` to set up the function

## Chapter 3

### Difference Between Functional & Unit Tests

**Functional Tests:** test the application from the outside, from the point of view of the user. 

**Unit tests:** test the application from the inside, from the point of view of the programmer.

**NOTE:** Functional tests should help you build an application with the right
functionality, and guarantee you never accidentally break it. Unit tests
should help you to write code that’s clean and bug free.

### Creating a Django `app` (in this case lists)

It's **incredibly** easy to create a Django `app` (that lives inside of a project)
using the `$python manage.py startapp <app_name>` syntax

Create an app within the `superlists` project called `lists`.

	$python manage.py startapp lists

Now the doc-tree looks like:

	├── db.sqlite3
	├── functional_tests.py
	├── lists
	│   ├── admin.py
	│   ├── __init__.py
	│   ├── migrations
	│   │   └── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   └── views.py
	├── manage.py
	└── superlists
	    ├── __init__.py
	    ├── settings.py
	    ├── urls.py
	    ├── wsgi.py


