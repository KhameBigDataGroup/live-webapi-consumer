## Cassandra tables:
----
### KeySpace
``` CREATE KEYSPACE bitcoin WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 2};```

### Blocks
``` CREATE TABLE bitcoin.blocks (hash text, confirmations int, strippedsize int, size int, weight int, height int, version int, version_hex text, merkleroot text, time int, mediantime int, nonce int, bits text, difficulty float, chainwork text, n_tx int, previousblockhash text, nextblockhash text, height int, PRIMARY KEY (hash, height));```

### Transactions

``` CREATE TABLE bitcoin.transactions (hash text PRIMARY KEY, version int, size int, vsize int, weight int, locktime int, vin text, vout text, block_height int, PRIMARY KEY (hash, block_height));```