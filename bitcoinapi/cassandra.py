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

def get_transactions_by_address(address):
    return session.execute(session.prepare('SELECT * FROM transactions WHERE vout LIKE "%?%";'),
                           (address,))


def get_latest_block_hash():
    return session.execute(session.prepare('SELECT max(height), hash FROM blocks'))[0].hash


def get_k_blocks(hash, k=10):
    if k <= 0:
        return []
    try:
        latest_block = get_blocks_by_hash([hash])[0]
    except:
        print("WARNING! block {} not found in cassandra".format(hash))
        return []
    return get_k_blocks(latest_block.previousblockhash, k - 1) + [latest_block]