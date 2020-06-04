import sys

def run():
    input = sys.argv[1]
    if input in ['new']:
        from install import run
        run(*sys.argv)
    elif input in ['deploy']:
        from deploy_run import run
        run(*sys.argv)
