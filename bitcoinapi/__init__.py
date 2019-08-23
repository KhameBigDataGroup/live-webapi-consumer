from bitcoinrpc.authproxy import AuthServiceProxy

from liveapi.settings import BITCOIN_USER, BITCOIN_PASSWORD


def get_bitcoin_rpc_connection():
    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (BITCOIN_USER, BITCOIN_PASSWORD))


