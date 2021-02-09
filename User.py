import Blockchain as bc

class User:
    def __init__(self):
        self.fname = fname
        self.lname = lname
        self.blockchain = None
        self.peers = []

    # allows user to send a digital media object (transaction) to their peers
    def upload(self, filename, title, date):
        bc.DigitalMedia(filename, title, date)

    # adds block to blockchain then sends out the block to the node's peers
    def mine(self):

    # allows user to find if the given file exists on the blockchain by hashing file and searching for the hash
    def find(self, filename):
