import Blockchain as bc
import Mediatypes as d
import Cryptography as c

#public_key, private_key = c.generate_public_private()
public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtgarh0ufy7jQxZg4Ev40\nxj4xVdoT+zQ6idjIhcv4KsZEG9BAuCQ/wWeaWiX4GYLR65zw9mYZXs5zQzuxN40E\ngySlBrhj+GMncuA2niFcOr2s+DDgjb5qXAp1cCeN5q9wgXB3Jk2f72LpXtXH8wjh\n6V83AIxcXgMGsLsG8nUGiAiUWKLL7IBu03Ojh2UTTQyOuqSDRwhqlX+OXYM7m2kr\ngbzUTiI2Ll0E4v9bqJ4p8XhB/jvKB194z/cD28uOiolZNTRgKbTw0tTgoRz3wfa1\nekzRmdgjZoyFfkD5CjTQIkNL5mPBX9GS1xxByctGxSi/DWccgWmXJQ8aZFxVIf8e\n/QIDAQAB\n-----END PUBLIC KEY-----'
private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAtgarh0ufy7jQxZg4Ev40xj4xVdoT+zQ6idjIhcv4KsZEG9BA\nuCQ/wWeaWiX4GYLR65zw9mYZXs5zQzuxN40EgySlBrhj+GMncuA2niFcOr2s+DDg\njb5qXAp1cCeN5q9wgXB3Jk2f72LpXtXH8wjh6V83AIxcXgMGsLsG8nUGiAiUWKLL\n7IBu03Ojh2UTTQyOuqSDRwhqlX+OXYM7m2krgbzUTiI2Ll0E4v9bqJ4p8XhB/jvK\nB194z/cD28uOiolZNTRgKbTw0tTgoRz3wfa1ekzRmdgjZoyFfkD5CjTQIkNL5mPB\nX9GS1xxByctGxSi/DWccgWmXJQ8aZFxVIf8e/QIDAQABAoIBACdf5P3UwYG/fkWn\n6kVNgNv7Ow/Ppy/ZOep0nte2af3SuovrrfxHNxVelFh4yyS1lDQr1EHwjv9fmDZM\ndMbH9dhqdlowS8vAoxlp39av77PzMLXVWNXAgWBckM/MdpkWjTcqvVNnSjftxP6T\nLvfnDXs+cfbn5dkePXXAVz3eS6XkG9KnExJe3XU8+imhHebqtELyrLVZr1tiEiFb\nO6xj/kLlX+1rwQWjCKXaDeUTaDv5ZYWGlInzYT6FZ16B4FJ6zQaWXXuKN/HKyLw0\nOfMy1M9Gstw6cdtGGTOJZ5aRbxIuGgi4Hbd0j8iD1K5p+dno62UpoLzwucXMnDPG\nlsJIRQECgYEA12J+Wm2g/rWg78NLpGDw8I9/RBfVEuDySsV5GIci0fKcfe18hzq5\n6lZ1s2WCchlPH+F4FtlgDMOkmw5CmLDXGlqm4udIxR7z25TK6bbOniILO28q90l1\nehUST82M2q9W0mpDGGXTLZSxxq6nVRlKithEzEFsT/UasJapqPuZjYECgYEA2FnQ\nzayGUxYYashPlG2i6iLSZxVMVxlfCQGASAPESLHit62SPGS05RAmc25TJEj+eu6r\nX+LnoIbQ6HT0sFIIbW+9xCg3d/PdEtOeclkwfO/61SneC38w8wVh7PbTQB3uLVr4\nZEqb4CJTINaiZAj6vTsHkkA72rruf88utm1mh30CgYAutrf82OYgGDiNh+fyAOyA\n4D6UAC9AZvVl7ipzfWu56UqzrTxjAAOupY3lmNCP+plEqtwm6IKCgjRDRPaAs2oT\n1zF26P7JcgslxsGzquhpN60D+Ppyo8YM8mEEWeqAy6KjBFUFB6CjtCpSkzLLrC6U\nqo9RVacuOFTPk/28HsWRAQKBgH0uesKGsLIidr5SaLlZNoqC23sJt8Ity+9KDw+c\nHlZxltzwcUzAeGqRja38h97W3WgD8OTqRVt8piPaiDn9PSMVJJf7LR0a3S+ngmZn\ndMbVlC0CrJe6YHg9BQw3RMQ0jTtxB4gAI3Dsa2z0w8Fd8LbNEPRudjN5NcZ9+mlT\no5+BAoGAcqBU5lBPFPhrwRu+bAS0nLfBKk2yS2s02UZsGA+KLkgNrwTFIgqCuPPA\n6iG+L/x52gBDp3lVGtvZoAIz3ovraHyipfNWwZrRxp5us4O0r9/2yi6cGF6QjSSa\ne4Yo304diVRRL5hZm92luGtdvQBHIlKbESG6n91wyFiAVjbm6W4=\n-----END RSA PRIVATE KEY-----'
#print("Public Key:", type(public_key), public_key)
#print("Private Key:", type(private_key), private_key)
l = [b'test1', b'test2', b'test3', b'test4']
h = c.string2bytes(c.merkle_root(l).hexdigest())
print("Hash:", type(h), h)

blockchain = bc.Blockchain()

media = d.Photo(h, b"Test Title", b"Test Description", b"2010/02/17", b"Eugene, OR")
source = bc.Source(media, public_key, private_key)
block1 = bc.Block(blockchain.head_block, [source])
blockchain.mine(block1, 0)

media2 = d.Photo(h, b"Test2", b"Testing the block", b"2021/02/17", b"Davey Jones Locker")
source2 = bc.Source(media2, public_key, private_key)
block2 = bc.Block(blockchain.head_block, [source2])
blockchain.mine(block2, 0)

