Python3 CRUD template
===============================

 Install `python3`, `pip`, `virtualenv`
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cp conf/config.ini.sample conf/config.ini
FLASK_DEBUG=1 FLASK_APP=run.py flask run
```
