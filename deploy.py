import paramiko, os, sys
from app.libs.yml_reader import YamlReader
from deploy.deployment_procedure import DeploymentProcedure

class Deploy:
    def __init__(self, *args, **kwargs):
        self.env = env = kwargs['environment']
        print('deploying %s' %(env))
        self.options = YamlReader(file='deploy/config.yml').read()[env]
        self.run()

    def run(self):
        client = paramiko.SSHClient()
        client._policy = paramiko.WarningPolicy()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(**self._config())

        # run deployment procedure
        # upload zipped package to server
        # unzip package and link config files
        # run migrations
        # run / restart supervisor

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
