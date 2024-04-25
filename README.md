# weather_forecast_api
A simple api to show weather

### Stack

* [Django](https://www.djangoproject.com/) as main web Framework


### Features
- [x] Search a city and get weather information

## Getting started

### Development

You need to have installed `git`, `python`, `poetry` and `django`.

1. Go to this [repo](https://github.com/EstebanSG/weather_forecast_api.git) and `git clone` the project localy.
2. `cd weather_forecast_api`.
3. Copy the `.env.example` to `.env` and fill the required variables.
4. Use `poetry install` to setup all dependencies.
5. Use `Make up` to migrate models and execute the server 
6. Open `localhost:8000` in your browser.
7. Start searching

### Setting Up a super_user for test usage (not required)

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuse
- or
      
       $ make create_user

Enter to `localhost:8000/admin/` to login
