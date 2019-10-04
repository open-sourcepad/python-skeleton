Sourcepad Skeleton Python Framework
===============================

## Getting Started
- Install `python3`, `pip`, `virtualenv`
- Activate virtualenv (eg. `source venv/bin/activate`)
- Create `conf/config.ini` (eg. `cp conf/config.ini.sample conf/config.ini`)
- Install dependencies `pip3 install -r requirements.txt`
- Run server `FLASK_DEBUG=1 FLASK_APP=main.py flask run`

## Running Tests
- nose2 -v package.module
> i.e. nose2 -v tests.app.api.home.view_test

## Coverage
- coverage run -m package.module
> i.e. coverage run -m tests.app.api.home.view_test

- coverage report package/module
> i.e. coverage report app/api/home/view.py
