require 'net/ssh/proxy/command'
require 'sshkit'
require 'sshkit/dsl'
include SSHKit::DSL


SSHKit.config.output_verbosity = :debug


SSHKit::Backend::Netssh.configure do |ssh|
  ssh.ssh_options = {
    proxy: Net::SSH::Proxy::Command.new('ssh -W %h:%p ec2-user@35.153.4.30')
  }
end

DIR = "/home/ubuntu/af-team-python"
SOCKFILE= "/home/ubuntu/af-team-python/gunicorn.socket"
BRANCH = "master"
WORKER_COUNT = 2

on 'ubuntu@10.0.2.253' do
  # execute "source #{DIR}/venv/bin/activate"
  execute "cd #{DIR} && git pull origin #{BRANCH} --force"
  #pkill -9 -f 'rb-fsevent|rails|spring|puma'
  # execute 'sudo pip3 install -r /home/deploy/af-python/requirements.txt'
  execute "kill -9 `ps aux | grep gunicorn | awk '{ print $2 }'`"
  execute "cd #{DIR} && source #{DIR}/venv/bin/activate && cd #{DIR} && gunicorn -w #{WORKER_COUNT} --bind=0.0.0.0:5002 --log-level=debug app.main:application --daemon"
end
