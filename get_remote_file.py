from fabric.api import get,env
env.hosts=['tabssum@10.236.61.136']
def get_file():
    get(remote_path="/tmp/data.txt",local_path="/tmp/")
