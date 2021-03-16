# CIS433Blockchain
 Fighting Fake News with Blockchain

-----------
### Table of Contents

1. [About the Project](#about-the-project)

	- [Built With](#built-with)

2. [Installation Instructions](#installation)

3. [User Guide](#user-guide)

4. [Contacts](#contacts)

## About the Project
A prototype Blockchain architecture that stores sources and media. \
Serves as a proof of concept that Blockchain can provide source traceability for digital media seen in news articles.

### Built With
The Blockchain is implemented in the python language, and utilizes the pycryptodome library for cryptographic features.

## Installation
In order to test what we have built so far, the pycryptodome library needs to be installed. 

pycryptodome can be installed by entering the following command into a terminal window.

`pip install pycryptodome`

see also: https://www.pycryptodome.org/en/latest/src/installation.html

## User Guide
We have a simple test script that can demonstrate the core functionality of the Blockchain.

Running `python3 test_user.py` will show the following:

1. Two users add each other as peers in the "network"
2. User1 uploads a photo to their Blockchain. This new block is then shared with user2
3. Both user1 and user2 find the photo on the Blockchain.
4. User2 uploads a second photo to the Blockchain. This new block is then shared with user1.
5. Both user1 and user2 find the photo on the Blockchain.
6. User1 tried to upload the photo user2 uploaded in step 4. This will not work since the photo hash already exists on the Blockchain.
7. User1 uploads a text file to the Blockchain.
8. User2 finds the text file on the Blockchain.

## Contact Us
Adam Christensen - christe2@uoregon.edu
Riley Matthews   - riley@cs.uoregon.edu