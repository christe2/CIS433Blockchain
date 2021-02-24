"""
Cryptography.py
Adam Christensen
Riley Matthews
Contains the cryptographic building blocks necessary for creating a blockchain
Libraries: Pycryptodome
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


def string2bytes(string):
    return bytes(string, 'utf-8')


def bytes2string(_bytes):
    return _bytes.decode('utf-8')


# merkle root helper function
def hash_list(lst):
    i = 0
    new_list = []
    while i < len(lst):
        if (i+1) == len(lst):
            hash1 = lst[i].digest()
            hash2 = b''
        else:
            hash1 = lst[i].digest()
            hash2 = lst[i+1].digest()
        _hash = hash1 + hash2
        new_list.append(SHA256.new(_hash))
        i += 2
    return new_list


# returns merkle root of list as type: Hash
def merkle_root(lst):
    new_list = []
    for l in lst:
        new_list.append(SHA256.new(l))
    while len(new_list) != 1:
        new_list = hash_list(new_list)
    return new_list[0]


def generate_public_private():
    """
    generate_public_private
        generates RSA public and private key
    :return
        returns public and private key. type: bytes
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key


def create_signature(lst, key):
    """
    create_signature
        creates a signature from a private key and a message
    :param
        mssg: the message to be decrypted. type: bytes.
        key: the key be used in the cipher. type: bytes
    :return
        returns a signature. type: bytes
    """
    h = merkle_root(lst)
    rsa_key = RSA.importKey(key)
    signature = pkcs1_15.new(rsa_key).sign(h)
    return signature


def check_signature(lst, signature, key):
    """
    check_signature
        checks a signature using a public key and a message
    :param
        mssg: the message the signature should contain. type: bytes.
        signature: the signature to be checked. type bytes
        key: the key be used in the cipher. type: bytes
    :return
        returns a signature. type: bytes
    """
    h = merkle_root(lst)
    rsa_key = RSA.importKey(key)
    try:
        pkcs1_15.new(rsa_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

