Python3 CRUD template
===============================

 Install `python3`, `pip`, `virtualenv`
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
flask db upgrade
flask run
```

List routes
```
python3 routes.py
python3 routes.py <search term>
e.g. python3 routes.py login
```
