import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from bitcoinapi import get_bitcoin_rpc_connection
from bitcoinapi.cassandra import get_blocks


@cache_page(5 * 60)
def get_status(r):
    rpc_connection = get_bitcoin_rpc_connection()
    chain_tx_stats = rpc_connection.getchaintxstats()
    blockchain_info = rpc_connection.getblockchaininfo()

    return JsonResponse({
        'lastBlockHeight': blockchain_info['blocks'],
        'totalTransactions': chain_tx_stats['txcount']
    })


# CREATE TABLE cycling.bitcoin_blocks ( hash text, height int, data text , PRIMARY KEY (hash, height));

def get_block(block_height):
    pass


# @cache_page(5 * 60)
def get_latest_blocks(r):
    rpc_connection = get_bitcoin_rpc_connection()
    blockchain_info = rpc_connection.getblockchaininfo()
    last_block_height = blockchain_info['blocks']

    block_heights = []
    for i in range(10):
        block_heights.append(last_block_height - i)

    cassandra_blocks = get_blocks(block_heights)

    blocks = []
    for block in cassandra_blocks:
        block_data = json.loads(block.data)
        blocks.append(block_data)
    return JsonResponse({
        'blocks': blocks
    })
