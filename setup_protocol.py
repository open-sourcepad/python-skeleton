import sys, os

def run():
    input = sys.argv[1]
    if input in ['new']:
        from install import run
        run(*sys.argv)
    elif input in ['deploy']:
        from deploy_run import run
        run(*sys.argv)
    elif input in ['routes']:
        finder = ''
        if len(sys.argv) == 3:
            finder = sys.argv[2]

        os.system(f"pipenv run python3 routes.py {finder}")
    elif input in ['run', 'serve', 'server', 's']:
        options = ' '.join(sys.argv[2:])
        os.system(f"pipenv run flask run {options}")
