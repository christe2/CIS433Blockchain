import hashlib
import datetime

class DigitalMedia:
    def __init__(self, file_hash, title, date):
        self.hash = None # hash of metadata and file_hash (should maybe be a merkle root?)
        self.file_hash = file_hash #hash of actual file
        # metadata
        self.title = title
        self.date = date

class Block:
    def __init__(self, data):
        self.index = 0
        self.data = data
        self.nonce = 0
        self.timeStamp = datetime.datetime.now()
        self.previous_hash = 0x0
        self.hash = None

    def __str__(self):
        return str(self.index) + "Block-Hash" + str(self.hash)

    def hash_block(self):
        data_as_string = self.__data_to_sting__()
        hashlib.sha256(data_as_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.genesis_block = Block("Genesis")
        self.head_block = self.genesis_block
        self.difficulty = 4  # number of 0s
        self.max_nonce = 2**32

    def proof_of_work(self):
        raise NotImplementedError

    def add(self, block):

