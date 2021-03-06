from __future__ import absolute_import
import os
from invoke import Collection, task
from trireme.migrators import cassandra, solr


@task
def setup():
    # Create the necessary directories
    directories = ['db', 'db/solr', 'db/migrations']
    for directory in directories:
        os.makedirs(directory)

ns = Collection(cassandra, solr)
ns.add_task(setup)
