# API SERVER

Written in Flask

## Configuration

.flaskenv - public variables
.env - private variables

## Setup Development

1. Create .env file to overwrite .public .flaskenv

1. Install dependencies

    ```
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
1. Run development server
   
    ```
    flask run
    ```
1. Go to server/ and run tests

    ```
    pytest -vv tests
    ```