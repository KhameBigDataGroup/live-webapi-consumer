import json
from time import time

from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from bitcoinapi.bitcoin import get_bitcoin_rpc_connection
from bitcoinapi.cassandra import get_blocks_by_height, get_blocks_by_hash, get_transactions_by_height, \
    get_transactions_by_hash, get_transactions_by_address, get_k_blocks, get_latest_block_hash, \
    get_transactions_by_block_hash
from bitcoinapi.utils import average_fee, total_fee


@cache_page(5 * 60)
def get_status(r):
    rpc_connection = get_bitcoin_rpc_connection()
    chain_tx_stats = rpc_connection.getchaintxstats()
    blockchain_info = rpc_connection.getblockchaininfo()

    return JsonResponse(blockchain_info)


@cache_page(5 * 60)
def get_latest_blocks(r):
    latest_hash = get_latest_block_hash()
    blocks = get_k_blocks(latest_hash)

    items = []
    for block in blocks:
        items.append({
            'height': block.height,
            'age': int(time() - int(block.time)),
            'transactions': block.n_tx,
            'average_fee': average_fee(json.loads(block.data[2:-1])),
            'size': block.size,
            'weight': block.weight,
            'hash': block.hash
        })

    return JsonResponse({'items': items})


@cache_page(5 * 60)
def get_transactions(request, block_hash):
    transactions = get_transactions_by_block_hash(block_hash)
    pagination = 30

    last_page = int(len(transactions) // pagination)
    page = min(int(request.GET.get('page', 1)), last_page)
    page = max(page, 1)

    try:
        start = (int(page) - 1) * pagination
        end = min(start + pagination, len(transactions))

        return JsonResponse({
            'page': page,
            'total': len(transactions),
            'start': start,
            'end': end,
            'has_next': page < last_page,
            'last_page': last_page,
            'transactions': transactions[start:end]
        })

    except ValueError:
        return JsonResponse({
            'transactions': []
        })


@cache_page(5 * 60)
def get_transaction_by_hash(r, hash):
    transaction = get_transactions_by_hash([hash])[0]

    return JsonResponse({
        'hash': transaction.hash,
        'block_height': transaction.block_height,
        'locktime': transaction.locktime,
        'size': transaction.size,
        'version': transaction.version,
        'vin': json.loads(transaction.vin[2:-1]),
        'vout': json.loads(transaction.vout[2:-1]),
        'vsize': transaction.vsize,
        'weight': transaction.weight
    })


@cache_page(5 * 60)
def get_block(r, hash):
    cassandra_blocks = get_blocks_by_hash([hash])

    if cassandra_blocks:
        block_data = json.loads(cassandra_blocks[0].data[2:-1])
    else:
        return HttpResponseNotFound()

    block_data['total_fee'] = total_fee(block_data)
    return JsonResponse(block_data)
