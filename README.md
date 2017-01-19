Flask Boilerplate
=====


[![Requirements Status](https://requires.io/github/pprmint/flask_boilerplate/requirements.svg?branch=master)](https://requires.io/github/pprmint/flask_boilerplate/requirements/?branch=master

Introduction
-----
A boilerplate for REST APIs implement using python flask. Ideal for doing micro services and API integrations.

#### Running the app
- Runs on Python 3.4+
- Install Python3 and pip3
- Install dependencies `pip3 install -r requirements.txt`
- Start the server `python3 run.py`

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

Contributing
-----
Push all the changes to your own branch before making a pull request to the master branch
###### New feature request
For adding new feature make sure to follow the following format for the pull request
- Title should be `feature/<feature_name>`
- Description should have the ff template
```
    ### Changes
        - change description
        - change description
    ### Testsing
        - List of tests done preferably with screenshots
    ### Contributor info
        - Name
        - Email
```

###### Fixing issues
For adding new feature make sure to follow the following format for the pull request
- Title should be `fix/<issue_that_needs_fixing>`
- Description should have the ff template
```
    ### Changes
        - change description
        - change description
    ### Testsing
        - List of tests done preferably with screenshots
    ### Contributor info
        - Name
        - Email
```
