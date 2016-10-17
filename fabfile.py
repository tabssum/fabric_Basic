from fabric.api import local
def local_usage():
    local("uname -a",capture=False)
