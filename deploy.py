import paramiko, os, sys, time

from datetime import datetime as DT
from pathlib import Path
from app.libs.yml_reader import YamlReader
from deploy.deployment_procedure import DeploymentProcedure

class Deploy:
    def __init__(self, *args, **kwargs):
        self.env = env = kwargs['environment']
        self.package_name = 'package'
        print('deploying %s' %(env))
        self.options = YamlReader(file='deploy/config.yml').read()[env]
        self.run()

    def run(self):
        dp = DeploymentProcedure(env=self.env, package_name=self.package_name)
        dp.run()

        # if not dp.error:
        #     client = self._connect()
        #     client.exec_command(f"mkdir {self.env}")
        #
        #
        #     ftp = client.open_sftp()
        #     ftp.put(f"{self._root_url}/package.tar.gz", f"/home/aptonomy/{self.env}/package.tar.gz")
        #
        #     self._command_execution(client, ['/home/aptonomy/.local/bin/pipenv --rm'], cd=f"{self.env}/current")
        #     self._command_execution(client, self._setup_commands, cd=self.env)
        #     self._command_execution(client, self._deploy_commands, cd=f"{self.env}/current")

    def _command_execution(self, client, cmds, cd):
        for cmd in cmds:
            cmd = f"cd {cd}; {cmd}"
            print(cmd)
            a, b, c = client.exec_command(cmd)

            print(c.read())

    def _connect(self):
        client = paramiko.SSHClient()
        client._policy = paramiko.WarningPolicy()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(**self._config())

        return client

    @property
    def _setup_commands(self):
        dt = DT.strftime(DT.now(), '%Y_%m_%d_%H_%I_%S')
        name = f"{self.package_name}_{dt}"
        return [
            f"mkdir revisions",
            f"tar -xvzf package.tar.gz -C revisions",
            f"mv revisions/{self.package_name} revisions/{name}",
            f"rm -rf current",
            f"ln -s revisions/{name}/ current",
        ]

    @property
    def _deploy_commands(self):
        return [
            "/home/aptonomy/.local/bin/pipenv install",
            "/home/aptonomy/.local/bin/pipenv update",
            # f"pipenv run flask db upgrade",
            "kill -9 `pgrep -f supervisord`",
            "/home/aptonomy/.local/bin/pipenv run supervisord",
            "/home/aptonomy/.local/bin/pipenv run supervisorctl stop all",
            "/home/aptonomy/.local/bin/pipenv run supervisorctl start all",
        ]

    @property
    def _root_url(self):
        url = os.path.abspath(__file__)
        return Path(url).parent

    def _ssh_config(self):
        ssh_config = paramiko.SSHConfig()
        user_config_file = os.path.expanduser(self.options['config'])
        if os.path.exists(user_config_file):
            with open(user_config_file) as f:
                ssh_config.parse(f)

        return ssh_config

    def _config(self):
        config = {'hostname': self.options['hostname'], 'username': self.options["username"]}
        ssh_config = self._ssh_config()

        user_config = ssh_config.lookup(config['hostname'])
        for k in ('hostname', 'username', 'port'):
            if k in user_config:
                config[k] = user_config[k]

        if 'proxycommand' in user_config:
            config['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

        return config


if __name__ == '__main__':
    Deploy(environment=sys.argv[1])
