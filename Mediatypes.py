"""
Mediatypes.py
Adam Christensen
Riley Matthews
Contains the different sources that can be put into the blockchain
"""


class Media:
    def __init__(self, file_hash, description):
        # hash of the source object (source+metadata+signature)
        self.file_hash = file_hash
        # metadata
        self.description = description

    def get_list(self):
        return [self.file_hash, self.description]


class Photo(Media):
    def __init__(self, file_hash, title, description, date, location, cc=b''):
        super().__init__(file_hash, description)
        # metadata
        self.title = title
        self.date = date
        self.location = location
        self.copyright = cc

    def get_list(self):
        return [self.file_hash, self.description, self.title, self.date, self.location, self.copyright]

"""
    def sign(self, key):


    def create_hash(self):
        self.hash = merkle_root([self.file_hash, self.title, self.description, self.date, self.copyright])
        return self.hash

    def check_hash(self):
        return self.hash == self.create_hash()
"""