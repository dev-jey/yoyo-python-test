# Yoyo Test APP

## Description
This is an app created as part of the Yoyo interview tests. It involves making an API call to an external weatherapi,
and calculating the forecasted minimum, maximum and average temperatures for a specific city, over a given period of time.

## Project File Structure
    -- yoyo_app
        -- configs
                __init__.py
                asgi.py
                settings.py
                urls.py
                wsgi.py
        -- temperature_api
                migrations
                __init__.py
                admin.py
                apps.py
                helpers.py
                models.py
                serializers.py
                tests.py
                urls.py
                views.py
        -- validators
                validators.py
    .env.sample
    .gitignore
    manage.py
    Pipfile
    README.md
    setup.cfg

## How to Install

#### Requirements
Ensure you have python 3.6+ installed in your local environment
1. clone the repository
    ```
    https://github.com/dev-jey/yoyo-python-test.git
    ```

2. Change directory to the yoyo-python-test directory
    ```
    cd yoyo-python-test
    ```

3. Install pipenv 
    ```
    pip install pipenv
    ```

4. Install required packages and dependencies
    ```
    pipenv shell & pipenv install
    ```
4. Rename the `.env.sample` file into `.env`, then replace the placeholder environment variables in the `.env` file with actual ones. Then run 
    ```
    source .env
    ```

6. Start the python server by running the following command, then test out the endpoint on postman `/api/locations/{city}/?days={number_of_days}`
    ```
    python manage.py runserver
    ```

6. Run linting and tests
    ```
    flake8 . & python manage.py test  && coverage report -m
    ```
## Documentation
Find the documentation for the project on `/api/docs`
## Technlogies & Packages Used
- Python v3.9
- Django
- Django Rest Framework (DRF)
- Flake8 & Autopep8
