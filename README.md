# API SERVER

Written in Flask

## Configuration

.flaskenv - public variables
.env - private variables

## Setup Development

1. Create `.env` file to overwrite public `.flaskenv` based on `.env-sample`

1. Install dependencies

    ```
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
1. Go to folder src and run development server and/or tests
   
    ```
    flask run
    pytest -vv tests
    ```