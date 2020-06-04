import os, sys
from pathlib import Path
from shutil import copytree, ignore_patterns
from distutils.dir_util import copy_tree

class Install:
    def __init__(self, *args, **kwargs):
        self.command = 'new'
        self.project_name = None
        self.args = args

        if len(self.args) == 3:
            self.command = self.args[1]
            self.project_name = self.args[2]


    def run(self):
        if len(self.args) < 3:
            print('not enough arguments')
            return False

        if self.project_name == '.':
            old_name = self.project_name
            new_name = f"{old_name}/tmp"

            self.project_name = new_name
            self._copy()
            os.popen('mv tmp/* .')
            os.popen('rm -rf tmp')
        else:
            self._copy()


    def _copy(self):
        to_path = f"{os.popen('pwd').read()}/{self.project_name}".replace('\n', '')

        from_path = self._root_url

        kwargs = dict(ignore=ignore_patterns(
            '__pycache__',
            '.pytest_cache',
            '*.pyc',
            'setup.py',
            '.gitignore',
            'install.py',
            '.git',
            '*.egg-info',
            'package*',
        ))

        try:
            copytree(from_path, to_path, **kwargs)
            print(f"Done creating project {to_path}")
        except Exception as e:
            print(f"Error:{e}")
            print('Sorry, a project/folder with the same name seems to be existing')
            print('Kindly put in another name or create the project within the folder')

    @property
    def _root_url(self):
        url = os.path.abspath(__file__)
        return Path(url).parent


def run(*args):
    Install(*args).run()
