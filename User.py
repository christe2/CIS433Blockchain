"""
User.py
Adam Christensen
Riley Matthews
Contains the different User types
"""

import Blockchain as bc
import Mediatypes as m
import Cryptography as c


class User:
    def __init__(self, name):
        self.name = name
        self.blockchain = bc.Blockchain()
        self.peers = []
        self.sources = []
        self.public_key = None
        self.private_key = None
        self.public_key, self.private_key = c.generate_public_private()

    def add_peer(self, peer):
        self.peers.append(peer)

    def random_peers(self, n):
        # returns a list of n random peers
        raise NotImplementedError

    def add_source(self, source):
        self.sources.append(source)
        #if len(self.sources) == self.blockchain.max_sources:
            #self.create_block()

    def add_block(self, block):
        if self.blockchain.add(block):
            print("New Block received. Block added to the Blockchain.")

    # allows user to send a digital media object (transaction) to their peers
    def upload(self, media_type, filename, title, description, date, location, cc=b''):
        if media_type.lower() == "photo":
            with open(filename, "rb") as image:
                f = image.read()
            file_hash = bytes(c.merkle_root([f]).hexdigest(), 'utf-8')
            media = m.Photo(file_hash, title, description, date, location, cc)
        else:
            print("Not a valid media type")
            return False
        source = bc.Source(media, self.public_key, self.private_key)
        self.sources.append(source)
        for peer in self.peers:
            peer.add_source(source)
        if len(self.sources) == self.blockchain.max_sources:
            self.create_block()
        return True

    def create_block(self):
        block = bc.Block(self.blockchain.head_block, self.sources)
        # for peer in self.peers:
        #   peer.receive_block(block)
        self.mine(block)

    # adds block to blockchain then sends out the block to the node's peers
    def mine(self, block):
        self.blockchain.mine(block, 0)
        print("Mining successful! Block added to the Blockchain.")
        for peer in self.peers:
            peer.add_block(block)

    # allows user to find if the given file exists on the blockchain by hashing file and searching for the hash
    def find(self, media_type, filename):
        if media_type.lower() == "photo":
            with open(filename, "rb") as image:
                f = image.read()
            file_hash = bytes(c.merkle_root([f]).hexdigest(), 'utf-8')
        else:
            print("Not a valid media type")
            return False
        block = self.blockchain.head_block
        while block != self.blockchain.genesis_block:
            for source in block.sources:
                if source.media.file_hash == file_hash:
                    print("Source was found.")
                    return source
            block = block.previous_block
        print("Source could not be found.")
        return None
