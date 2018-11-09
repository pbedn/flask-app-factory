# API SERVER

Simple API written in Flask using application factory setup and modular structure with Blueprints

## Configuration

> .env - private environmental variables (secret_key) and flask run env

> settings.py - public configuration

## Setup Development

1. Create `.env` file based on `.env-sample`
    ```
    FLASK_APP="server:create_app('server.settings.ProductionConfig')" -> see settings.py
    FLASK_ENV=production/development
    SECRET_KEY=VERY_LONG_SECRET_12345
    ```

1. Install dependencies
    ```
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
1. Go to folder server and run development server and/or tests
    ```
    flask run
    pytest -vv tests
    ```
    
    ---
    
    Ideas for project layout and code are from [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation)
