from fabric.api import env,run
env.hosts=['tabssum@10.236.61.135','tabssum@10.236.61.136']
def uptime():
    result=run('ls -s')
