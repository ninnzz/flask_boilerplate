Sample App
=====

Introduction
-----
A boilerplate for REST APIs implement using python flask.

#### Project Structure
```
    +-- app/
    |   +-- api/
    |   |   +-- module/
    |   |   |   +-- __init__.py
    |   |   |   +-- dispatch.py
    |   |   |   +-- model.py
    |   +-- conf/
    |   |   +-- env/
    |   |   |   +-- __init__.py
    |   |   |   +-- development.py
    |   |   |   +-- staging.py
    |   |   |   +-- production.py
    |   |   +-- __init__.py
    |   |   +-- config.py
    |   |   +-- constants.py
    |   +-- lib/
    |   |   +-- __init__.py
    |   |   +-- database.py
    |   |   +-- decorators.py
    |   |   +-- error_handler.py
    |   |   +-- response.py
    |   +-- util/
    |   |   +-- __init__.py
    |   |   +-- utils.py
    |   +-- www/
    |   |   +-- assets/
    |   |   +-- pages/
    |   +-- app.py
    |   +-- __init__.py
    +-- data/
    |   +-- schema.sql
    |   +-- seed.sql
    +-- README.md
    +-- requirements.txt
    +-- run.py
    +-- setup.py
```


#### Implementing a module
```
    +-- module/
    |   +-- __init__.py
    |   +-- dispatch.py
    |   +-- model.py
```
###### dispatch
Dispatch is where you store all the request related context. The following are handled by `dispatch.py`
- reuqest handling
- response handling
- routing of request
- authentication

We need to make sure that the request context does not mix with any of the app logic.

###### model
Model is the the one that handles the transactional operations.
- Insert
- Update
- Get
- Search
- Delete