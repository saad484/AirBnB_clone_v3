# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# """
# @author: saad484

# """
# #from fabric import Connection, Config, task

# from datetime import datetime

# env.user = 'ubuntu'
# env.hosts = ['100.26.53.206	', '52.86.39.252']


# def do_pack():
#     """
#     Targging project directory into a packages as .tgz
#     """
#     now = datetime.now().strftime("%Y%m%d%H%M%S")
#     local('sudo mkdir -p ./versions')
#     path = './versions/web_static_{}'.format(now)
#     local('sudo tar -czvf {}.tgz web_static'.format(path))
#     name = '{}.tgz'.format(path)
#     if name:
#         return name
#     else:
#         return None


# def do_deploy(archive_path):
#     """Deploy the boxing package tgz file
#     """
#     try:
#         archive = archive_path.split('/')[-1]
#         path = '/data/web_static/releases/' + archive.strip('.tgz')
#         current = '/data/web_static/current'
#         put(archive_path, '/tmp')
#         run('mkdir -p {}'.format(path))
#         run('tar -xzf /tmp/{} -C {}'.format(archive, path))
#         run('rm /tmp/{}'.format(archive))
#         run('mv {}/web_static/* {}'.format(path, path))
#         run('rm -rf {}/web_static'.format(path))
#         run('rm -rf {}'.format(current))
#         run('ln -s {} {}'.format(path, current))
#         print('New version deployed!')
#         return True
#     except:
#         return False


# def deploy():
#     """
#     A function to call do_pack and do_deploy
#     """
#     archive_path = do_pack()
#     answer = do_deploy(archive_path)
#     return answer

from fabric import Connection, Config, task
from datetime import datetime
@task
def do_pack(c):
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    c.run('mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    c.run('tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None

@task
def do_deploy(c, archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        c.put(archive_path, '/tmp')
        c.run('mkdir -p {}'.format(path))
        c.run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        c.run('rm /tmp/{}'.format(archive))
        c.run('mv {}/web_static/* {}'.format(path, path))
        c.run('rm -rf {}/web_static'.format(path))
        c.run('rm -rf {}'.format(current))
        c.run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False

@task
def deploy(c):
    """
    A function to call do_pack and do_deploy
    """
    archive_path = do_pack(c)
    answer = do_deploy(c, archive_path)

# Entry point to run the 'deploy' task
if __name__ == '__main__':
    deploy(Connection('ubuntu@100.26.53.206'))
