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

Framework installation
```
cd python-skeleton
git pull --rebase
pip3 install -e .
```

Framework usage
```
if no project / folder existing
> dyao new <project_name>

if project exists
> cd <project_name>
> dyao new .

NOTE:
Same folder/project name is not allowed and will return an error message
This is to avoid unneccessarily overwriting existing projects
```

Deployment
```
pipenv run dyao_deploy <environment>

if that doesn't work
pipenv run python3 deploy_run.py <environment>
```
