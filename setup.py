from distutils.core import setup
setup(
  name = 'master_slave_router',
  packages = ['master_slave_router'],
  version = '0.1',
  description = 'A simple master-slave database router that can route all reads to slave(s) and writes to a master database.',
  author = 'Abhinav I',
  author_email = 'abhinav.qd@gmail.com',
  url = 'https://github.com/code-haven/django-master-slave-router',
  download_url = 'https://github.com/code-haven/django-master-slave-router/tarball/0.1',
  keywords = ['django', 'master', 'slave', 'database', 'router'],
  classifiers = [],
)