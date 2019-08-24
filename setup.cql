CREATE KEYSPACE IF NOT EXISTS bitcoin WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE bitcoin;

CREATE TABLE IF NOT EXISTS bitcoin.blocks(hash text, confirmations int, strippedsize int, size int, weight int, height int, version int, version_hex text, merkleroot text, time int, mediantime int, nonce int, bits text, difficulty float, chainwork text, n_tx int, previousblockhash text, nextblockhash text, height int, PRIMARY KEY (hash, height));

CREATE TABLE IF NOT EXISTS bitcoin.transactions (hash text PRIMARY KEY, version int, size int, vsize int, weight int, locktime int, vin text, vout text, block_height int, PRIMARY KEY (hash, block_height));

CREATE CUSTOM INDEX vout_details ON bitcoin.transactions (vout) USING 'org.apache.cassandra.index.sasi.SASIIndex' WITH OPTIONS = { 'mode': 'CONTAINS', 'analyzer_class': 'org.apache.cassandra.index.sasi.analyzer.NonTokenizingAnalyzer', 'case_sensitive': 'false'};
