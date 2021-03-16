"""
Mediatypes.py
Adam Christensen
Riley Matthews
Contains the different media that can be put into the blockchain
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

# TODO: implement in upload function
class Video(Media):
    def __init__(self, file_hash, title, description, date, location, cc=b''):
        super().__init__(file_hash, description)
        # metadata
        self.title = title
        self.date = date
        self.location = location
        self.copyright = cc

        # video specific metadata?
        # length?

    def get_list(self):
        return [self.file_hash, self.description, self.title, self.date, self.location, self.copyright]


class Text(Media):
    def __init__(self, file_hash, title, description, date, cc=b''):
        super().__init__(file_hash, description)
        # metadata
        self.title = title
        self.date = date
        #self.location = location
        self.copyright = cc

        # text specific metadata?

    def get_list(self):
        return [self.file_hash, self.description, self.title, self.date, self.copyright]