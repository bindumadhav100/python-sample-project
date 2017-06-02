# python-sample-project
A Sample Project to be used for examples in https://ralphavalon.wordpress.com/ and https://ralphavalonbr.wordpress.com/

### How to configure ###
* Execute the command:
```
pip install -r requirements.txt
```

### About the project ###

* It's a simple project with Flask exposing 4 endpoints:
```
/
/create
/rest/
/rest/:user_id
```

* Base path: **http://localhost:8081/**

* The project is about adding and getting users only, but of two ways: *web page* and *REST*.

* **NOTE:** This branch uses a python list as database. Other branches will have SQLAlchemy to use with any database.

* **START THE PROJECT:**
```
python app.py
```