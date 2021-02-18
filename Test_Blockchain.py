import Blockchain as bc


l = ['test1', 'test2', 'test3', 'test4']
h = bc.merkle_root(l)
print(h)
blockchain = bc.Blockchain()
prev_hash = blockchain.head_block.hash
digital_media = bc.DigitalMedia(h, "Test", "Testing the block", "2010/02/17")
block1 = bc.Block(digital_media, blockchain.head_block)
block1.mine(0, 2, 3)
blockchain.add(block1)
print(block1)

digital_media2 = bc.DigitalMedia(h, "Test", "Testing the block", "2021/02/17")
block2 = bc.Block(digital_media2, blockchain.head_block)
block2.mine(0, 0, 3)
blockchain.add(block2)
print(block2)

print("2021/02/17 to 2021/02/16")
block1.data.date = "2021/02/16"
print(block1)
print(block2)