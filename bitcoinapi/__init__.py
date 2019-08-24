from bitcoinrpc.authproxy import AuthServiceProxy

from liveapi.settings import BITCOIN_USER, BITCOIN_PASSWORD, BITCOIN_HOST, BITCOIN_PORT


def get_bitcoin_rpc_connection():
    return AuthServiceProxy("http://%s:%s@%s:%s" % (BITCOIN_USER, BITCOIN_PASSWORD, BITCOIN_HOST, BITCOIN_PORT))


