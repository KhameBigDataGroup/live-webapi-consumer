from cassandra.cluster import Cluster
from cassandra.query import ValueSequence

from liveapi.settings import BTC_KEYSPACE, CASSANDRA_HOST, CASSANDRA_PORT

cluster = Cluster([CASSANDRA_HOST], port=CASSANDRA_PORT)
session = cluster.connect('cycling', wait_for_all_pools=True)
session.set_keyspace(BTC_KEYSPACE)


def get_blocks(ids):
    return session.execute(session.prepare('SELECT * FROM bitcoin_blocks where height in ?'),
                           (ValueSequence(ids),))
