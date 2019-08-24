import json
from time import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from bitcoinapi.bitcoin import get_bitcoin_rpc_connection
from bitcoinapi.cassandra import get_blocks_by_height, get_blocks_by_hash, get_transactions_by_height, \
    get_transactions_by_hash, get_transactions_by_address, get_k_blocks, get_latest_block_hash


@cache_page(5 * 60)
def get_status(r):
    rpc_connection = get_bitcoin_rpc_connection()
    chain_tx_stats = rpc_connection.getchaintxstats()
    blockchain_info = rpc_connection.getblockchaininfo()

    return JsonResponse({
        'lastBlockHeight': blockchain_info['blocks'],
        'totalTransactions': chain_tx_stats['txcount']
    })

# @cache_page(5 * 60)
def get_latest_blocks(r):
    latest_hash = get_latest_block_hash()
    blocks = get_k_blocks(latest_hash)

    items = []
    for block in blocks:
        items.append({
            'height': block.height,
            'age': int(time() - int(block.time)),
            'transactions': block.n_tx,
            'average_fee': 0,
            'size': block.size,
            'weight': block.weight,
            'hash': block.hash
        })

    return JsonResponse({'items': items})

# @cache_page(5 * 60)
def get_transactions(r, block_height):
    cassandra_transactions = get_transactions_by_height([block_height])
    page = request.GET.get('page', '1')
    pagination = request.GET.get('pagination', '50')

    try:
        start = (int(page) - 1) * int(pagination)
        end = start + int(pagination)
        transactions = cassandra_transactions[start:end]

        return JsonResponse({
            'transactions': transactions
        })

    except ValueError:
        return JsonResponse({
            'transactions': []
        })

# @cache_page(5 * 60)
def get_transactions_address(r, address):
    cassandra_transactions = get_transactions_by_address(address)
    page = request.GET.get('page', '1')
    pagination = request.GET.get('pagination', '50')

    try:
        start = (int(page) - 1) * int(pagination)
        end = start + int(pagination)
        transactions = cassandra_transactions[start:end]

        return JsonResponse({
            'transactions': transactions
        })

    except ValueError:
        return JsonResponse({
            'transactions': []
        })
        
# @cache_page(5 * 60)
def get_transaction_by_hash(r, hash):
    transactions = get_transactions_by_hash([hash])

    return JsonResponse({
        'transactions': transactions
    })

# @cache_page(5 * 60)
def get_block(r, height):
    cassandra_blocks = get_blocks_by_height([height])

    block_data = ''
    if cassandra_blocks:
        block_data = cassandra_blocks[0]
    
    return JsonResponse({
        'block': block_data
    })

