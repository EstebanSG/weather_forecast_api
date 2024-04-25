# Define el comando `make migrations`
migrations:
	python manage.py makemigrations

# Define el comando `make migrate`
migrate:
	python manage.py migrate

create_user:
	python manage.py createsuperuser

shell:
	python manage.py shell

runserver:
	python manage.py runserver


up: migrate runserver

test:
	python manage.py test