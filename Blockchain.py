from Crypto.Hash import SHA256
import datetime as dt


# merkle root helper function
def hash_list(l):
    i = 0
    new_list = []
    while i < len(l):
        if (i+1) == len(l):
            x2 = ''
        else:
            x2 = l[i+1]
        x = l[i] + x2
        new_list.append(SHA256.new(data=bytes(x, 'utf-8')).hexdigest())
        i += 2
    return new_list


# returns merkle root as type: string
def merkle_root(lst):
    while len(lst) != 1:
        lst = hash_list(lst)
    return lst[0]


class DigitalMedia:
    def __init__(self, file_hash, title, description, date, cc=''):
        # hash of metadata and file_hash (should maybe be a merkle root?)
        self.hash = None
        # hash of digital media file
        self.file_hash = file_hash
        # metadata
        self.title = title
        self.description = description
        self.date = date
        self.copyright = cc
        self.create_hash()

    def create_hash(self):
        self.hash = merkle_root([self.file_hash, self.title, self.description, self.date, self.copyright])
        return self.hash

    def check_hash(self):
        return self.hash == self.create_hash()


class GenesisBlock:
    def __init__(self):
        self.previous_block = None
        self.index = 0
        self.data = DigitalMedia('', "Genesis Block", "The first block in the blockchain", "1970/1/1")
        self.nonce = 0
        self.timeStamp = "1970/1/1"
        self.previous_hash = ''
        self.hash = None

    def __str__(self):
        self.hash_block()
        return str(self.index) + " Block-Hash: " + str(self.hash) + ' ' + str(self.previous_hash)

    def check_hash(self, difficulty):
        return int(self.hash, 16) >> (64-difficulty)*4 == 0

    def hash_block(self):
        self.hash = merkle_root([str(self.index), self.data.create_hash(), str(self.nonce), str(self.timeStamp),
                                 self.previous_hash, str(self.previous_block)])

    def mine(self, init_vec, max_nonce, difficulty):
        self.nonce = init_vec
        self.hash_block()
        while int(self.hash, 16) >> (64-difficulty)*4 != 0:
            self.nonce += 1
            self.hash_block()
        #print(self.nonce)
        #print(self.hash)


class Block:
    def __init__(self, data, previous_block):
        self.previous_block = previous_block
        self.index = previous_block.index + 1
        self.data = data
        self.nonce = 0
        self.timeStamp = dt.datetime.now()
        self.previous_hash = self.previous_block.hash
        self.hash = None

    def __str__(self):
        self.previous_hash = self.previous_block.hash
        self.hash_block()
        return str(self.index) + " Block-Hash: " + str(self.hash) + " Prev-Hash: " + str(self.previous_hash)

    def check_hash(self, difficulty):
        return int(self.hash, 16) >> (64 - difficulty) * 4 == 0

    def hash_block(self):
        self.previous_hash = self.previous_block.hash
        self.hash = merkle_root([str(self.index), self.data.create_hash(), str(self.nonce), str(self.timeStamp),
                                     self.previous_hash])  # str(self.previous_block)]

    def mine(self, init_vec, max_nonce, difficulty):
        self.nonce = init_vec
        self.hash_block()
        while int(self.hash, 16) >> (64 - difficulty) * 4 != 0:
            self.nonce += 1
            self.hash_block()
        # print(self.nonce)
        # print(self.hash)


class Blockchain:
    def __init__(self):
        self.genesis_block = GenesisBlock()
        self.head_block = self.genesis_block
        self.difficulty = 3  # number of 0s
        self.max_nonce = 2**32
        self.genesis_block.mine(7831293, 0, 6)

    def proof_of_work(self):
        raise NotImplementedError

    def check_block(self, block):
        if block.previous_hash == self.head_block.hash and block.check_hash(self.difficulty):
            return True
        else:
            return False

    def add(self, block):
        if self.check_block(block):
            self.head_block = block
            print("Block successfully added")
            return True
        else:
            print("Not a viable block")
            return False
