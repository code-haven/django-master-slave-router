# django-master-slave-router
---
A simple database router that lets you route all reads to slave(s) and writes to a master database in a django project. It **DOES NOT** take care of replication nor does it handle scenarios where your databases are down/unavailable.

## Installation

Install the package through pip.

    pip install django-master-slave-router

Prerequisites:

  * Django >= 1.5


## Usage

Add the following settings inside your project's **settings.py**

1) Add 'master\_slave_router' to INSTALLED\_APPS.

    INSTALLED_APPS = (
        ...
        'master_slave_router',
    )

2) Add MasterSlaveRouter to DATABASE_ROUTERS

    DATABASE_ROUTERS = ('master_slave_router.MasterSlaveRouter')


3) Add connection settings for slave/master databases.

    DATABASES = {
        'default': {
            ...
            },

        'test_slave_1': {
            ...
            },

        'test_slave_2': {
            ...
            }
    }

4) Specify name(s) of the master and slave connections.

    SLAVE_DATABASES = ('test_slave1', 'test_slave2')
    MASTER_DATABASE = 'default'



## Licence
MIT.