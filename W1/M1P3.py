import hashlib


# Blockchain mining
# the hash of Block[i+1] begins with seed

class Block:
    def __init__(self, index, timestamp, data, prevhash, nonce):
        self.index = index
        self.timestamp = timestamp #this should be in format strftime(%Y-%m-%d, %H:%M:%S")
        self.data = data
        self.prevhash = prevhash
        self.nonce = nonce
        self.hash = hashlib.sha256(f'{index}-{timestamp}-{data}-{prevhash}-{nonce}'.encode('utf-8')).hexdigest()

# Implement mining
# mine = “ nd nonce s.t. H(PrevHash || tx_ROOT || nonce) starts with 17 zeroes”
def mine(block, lz):
    #prefix = '0' * lz
    prefix = "0000"
    index = block.index
    timestamp = block.timestamp
    data = block.data
    prevhash = block.prevhash
    nonce = 0
    hash = block.hash
    while not (str(prevhash).startswith(prefix) or str(hash).startswith(prefix)):
        nonce += 1
        hash = hashlib.sha256(f'{index}-{timestamp}-{data}-{prevhash}-{nonce}'.encode('utf-8')).hexdigest()
    print(hash)

# Connect to server
#eitn41.eit.lth.se:3152/generate?seed=1234

# Mine 3 blocks
# hash of a Block is defined as the hexdigest of sha256 with input all of the entries of a block

# Submit blockchain

#eitn41.eit.lth.se:3152/submit?seed=YOUR_SEED&chain=YOUR_CHAIN

if __name__ == "__main__":
    blocks = [{"block_id": 0, "time_stamp": "2022-12-14, 19:18:33", "meta_data": "GENESIS BLOCK", "prev_hash": "0", "hash_salt": 1096670514943, "curr_hash": "00001d08fe4d39bd1b53bfd1e8a5d4b9032336d0289eefd232b5e57915bfe90e"}, {"block_id": 1, "time_stamp": "2022-12-14, 19:18:34", "meta_data": "block1", "prev_hash": "00001d08fe4d39bd1b53bfd1e8a5d4b9032336d0289eefd232b5e57915bfe90e", "hash_salt": 389669136478, "curr_hash": "0000e9f7be9dc30d039a94abf0880b7eeb2a8adacea4eaec2721551a9484d8f4"}]
    blocks_class = [Block(block["block_id"], block["time_stamp"], block["meta_data"], block["prev_hash"], block["curr_hash"]) for block in blocks]
    num_generated_blocks = 0
    while num_generated_blocks < 3:
        mine(blocks_class[0], 17)
        num_generated_blocks += 1