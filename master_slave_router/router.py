from django.conf import settings
from itertools import cycle


"""
The slave database is selected in a round-robin pattern. If there are no slave databases listed, we will use master
for all operations.

Slave databases are defined in settings.SLAVE_DATABASES as a tuple of the slave database connection names.
Master database is defined in settings.MASTER_DATABASE, which by default is 'default'.
"""
HAS_SLAVES = False
if settings.has_attr('SLAVE_DATABASES'):
    HAS_SLAVES = True
    SLAVE_DATABASE = cycle(settings.SLAVE_DATABASES)

if settings.has_attr('MASTER_DATABASE'):
    MASTER_DATABASE = settings.MASTER_DATABASE
else:
    MASTER_DATABASE = 'default'


class MasterSlaveRouter(object):
    """
    A simple database router that directs all reads to the slave database(s) and writes to the master.
    If there are multiple slave databases, it will select them in a round-robin pattern.
    """
    def db_for_read(self, *args):
        """
        Decides which database is to be selected for the read operation.
        """
        if HAS_SLAVES:
            return next(SLAVE_DATABASE)
        else:
            return settings.MASTER_DATABASE

    def db_for_write(self, *args):
        """
        Decides which database is to be selected for the write operation
        """
        return settings.MASTER_DATABASE

    def allow_relation(self, *args):
        """
        Always allow relations as all the read operations are done on the slave databases.
        """
        return True

    def allow_migrate(self, database, *args):
        """
        Allow migrations only if db is master.
        """
        if database == settings.MASTER_DATABASE:
            return True
        return None
