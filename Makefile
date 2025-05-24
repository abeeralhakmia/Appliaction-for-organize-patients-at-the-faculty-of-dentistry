format:
	isort .
	black .

shell:
	python bloodbank\manage.py shell_plus

mm:
	python bloodbank\manage.py makemigrations

m:
	python bloodbank\manage.py migrate

mmm: mm m
