from cassandra.cluster import Cluster
from cassandra.query import ValueSequence

from liveapi.settings import BTC_KEYSPACE, CASSANDRA_HOST, CASSANDRA_PORT

cluster = Cluster([CASSANDRA_HOST], port=CASSANDRA_PORT)
session = cluster.connect()
session.set_keyspace(BTC_KEYSPACE)


def get_blocks_by_height(ids):
    return session.execute(session.prepare('SELECT * FROM blocks where height in ?'),
                           (ValueSequence(ids),))

def get_blocks_by_hash(hash):
    return session.execute(session.prepare('SELECT * FROM blocks where hash in ?'),
                           (ValueSequence(hash),))

def get_transactions_by_height(ids):
    return session.execute(session.prepare('SELECT * FROM transactions where block_height in ?'),
                           (ValueSequence(ids),))

def get_transactions_by_hash(hash):
    return session.execute(session.prepare('SELECT * FROM transactions where hash in ?'),
                           (ValueSequence(hash),))

    