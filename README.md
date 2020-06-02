Python3 CRUD template
===============================

 Install `python3`, `pip`, `pipenv`
```
pipenv --python 3
pipenv install -d
cp .env.sample .env
```

Run / Migrate app as pipenv
```
pipenv run flask db upgrade
pipenv run flask run
```

Run / Migrate app in virtual environment
```
source `pipenv --venv`/bin/activate
flask db upgrade
flask run
```

List routes
```
python3 routes.py
python3 routes.py <search term>
e.g. python3 routes.py login
```
