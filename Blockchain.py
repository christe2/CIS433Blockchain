"""
Blockchain.py
Adam Christensen
Riley Matthews
Contains the components of the blockchain: Source, Block, Blockchain
"""

import Cryptography as c
import Mediatypes as d
import datetime as dt


class Source:
    """
    The unit of storage for our media tracking blockchain (our equivalent of a bitcoin transaction)
    """
    def __init__(self, media, public_key, private_key):
        self.hash = None
        self.media = media
        self.public_key = public_key
        self.signature = None
        self.sign(private_key)
        self.create_hash()

    # creates a signature from the given key
    def sign(self, private_key):
        self.signature = c.create_signature(self.media.get_list(), private_key)

    def get_list(self):
        return self.media.get_list() + [self.public_key, self.signature]

    # creates a hash of the source
    def create_hash(self):
        self.hash = bytes(c.merkle_root(self.get_list()).hexdigest(), 'utf-8')

    def check_signature(self):
        return c.check_signature(self.media.get_list(), self.signature, self.public_key)

    # check if the hash and the signature are valid
    def check_source(self):
        if self.hash == bytes(c.merkle_root(self.get_list()).hexdigest(), 'utf-8'):
            if self.check_signature():
                return True
            else:
                print("Source Error. Invalid signature")
                return False
        else:
            print("Source Error. Invalid hash:")
            return False


class Block:
    def __init__(self, previous_block, sources):
        self.previous_block = previous_block
        self.index = previous_block.index + 1
        self.max_sources = 1
        self.sources = []
        self.nonce = 0
        self.timeStamp = dt.datetime.now()
        self.previous_hash = self.previous_block.hash
        self.hash = None
        for source in sources:
            self.sources.append(source)

    def get_list(self):
        lst = [bytes(self.index), bytes(self.nonce), bytes(str(self.timeStamp), 'utf-8'), self.previous_hash]
        for source in self.sources:
            lst.append(source.hash)
        return lst

    def add_source(self, source):
        if len(self.sources) < self.max_sources:
            if source.check_source():
                self.sources.append(source)
                return True
            else:
                print("Add source error. Invalid source")
                return False
        else:
            print("Add source error. Block is full.")
            return False

    def check_sources(self):
        for source in self.sources:
            if not source.check_source():
                print("Check source error. Not a viable Source.")
                return False
            else:
                return True

    def hash_block(self):
        self.hash = bytes(c.merkle_root(self.get_list()).hexdigest(), 'utf-8')

    def check_hash(self, difficulty):
        if int(self.hash, 16) >> (64 - difficulty) * 4 == 0:
            if self.hash == bytes(c.merkle_root(self.get_list()).hexdigest(), 'utf-8'):
                return True
            else:
                return False
        else:
            return False


class GenesisBlock:
    def __init__(self):
        self.previous_block = None
        self.index = 0
        self.sources = b'0'
        self.nonce = 0
        self.timeStamp = b'1970/1/1'
        self.previous_hash = b'0'
        self.hash = b'0000000000'


class Blockchain:
    def __init__(self):
        self.genesis_block = GenesisBlock()
        self.head_block = self.genesis_block
        self.difficulty = 3  # number of 0s
        self.max_nonce = 2**32
        self.max_sources = 1

    def mine(self, block, init_vec):
        block.nonce = init_vec
        block.hash_block()
        while int(block.hash, 16) >> (64 - self.difficulty) * 4 != 0:
            block.nonce += 1
            block.hash_block()
        self.head_block = block
        print("nonce:", block.nonce)
        print("hash:", block.hash)

    def check_block(self, block):
        if block.previous_hash == self.head_block.hash:
            if block.check_hash(self.difficulty):
                return True
            else:
                print("Failed hash check")
                return False
        else:
            print("previous hash != head block hash")
            return False

    def add(self, block):
        if self.check_block(block):
            self.head_block = block
            #print("Block successfully added")
            return True
        else:
            print("Not a viable block")
            return False

