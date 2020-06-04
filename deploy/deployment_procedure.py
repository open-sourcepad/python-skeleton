import os, tarfile

from shutil import copytree, rmtree, ignore_patterns, copy
from pathlib import Path

class DeploymentProcedure:
    def __init__(self, **kwargs):
        self.package_name = kwargs.get('package_name', 'package')
        self.env = kwargs.get('env', 'staging')
        self.error = False

    def run(self):
        self._create_package_folder()
        self._copy_files()

        if not self.error:
            self._zip()

    def _zip(self):
        print("Creating zip file")

        try:
            # from_path = f"{self._root_url}/{self.package_name}"
            # to_path = f"{self._root_url}/{self.package_name}.tar.gz"

            from_path = f"{self.package_name}"
            to_path = f"{self.package_name}.tar.gz"

            if os.path.isfile(to_path):
                os.remove(to_path)

            tar = tarfile.open(to_path, 'w:gz')
            tar.add(from_path)
            tar.close()

            print(f"Done: {to_path}")
        except Exception as e:
            print(f"\t\tZip process error: {e}")

    def _create_package_folder(self):
        print('creating package')
        if not os.path.exists(self.package_name):
            os.makedirs(self.package_name)
            print(f"Done: {self.package_name}")
            return

        print(f"Already exists: {self.package_name}")


    def _copy_dir(self):
        try:
            for name in self._copy_list:
                self._copy_procedure(name)
        except Exception as e:
            raise

    def _copy_files(self):
        self._loop_through(self._list_dir, copytree)

        if self.error:
            return False

        self._loop_through(self._list_files, copy)

        if self.error:
            return False

        self._copy_procedure(f"deploy/.env.{self.env}", copy, '.env')
        self._copy_procedure(f"deploy/supervisord.conf.{self.env}", copy, 'supervisord.conf')

    def _loop_through(self, list_data, protocol=copy):
        for value in list_data:
            self._copy_procedure(value, protocol)
            if self.error:
                return False

    @property
    def _list_dir(self):
        return [
            'app'
        ]

    @property
    def _list_files(self):
        return [
            'config.py',
            'Pipfile',
            'Pipfile.lock',
            'routes.py',
            'run.py'
        ]

    def _copy_procedure(self, path, protocol=copy, rename=None):
        try:
            print(f"Creating {path}")
            from_path = f"{self._root_url}/{path}"

            if rename:
                print(f"Renamed {path} to {rename}")
                path = rename

            to_path = f"{self._root_url}/{self.package_name}/{path}"

            if '.' in path or 'Pipfile' in path:
                if os.path.isfile(to_path):
                    os.remove(to_path)
            else:
                if os.path.exists(to_path):
                    rmtree(to_path)

            kwargs = {}

            if protocol == copytree:
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

            protocol(from_path, to_path, **kwargs)
            print(f"Done: {path}")

        except Exception as e:
            print(f"\t\t{path} Does not exists\n\t\tError: {e}")
            self.error = True
            return False

    @property
    def _root_url(self):
        url = os.path.abspath(os.path.dirname(__file__))
        return Path(url).parent
