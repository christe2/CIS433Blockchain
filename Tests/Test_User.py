import User as u

user1 = u.User("Adam Christensen")
user2 = u.User("Riley Matthews")
user1.add_peer(user2)
user2.add_peer(user1)

user1.upload("PhoTo", 'GreeceProtest2012.jpg', b"Greece Protest",
          b"Protesters during a violent anti-austerity demonstration", b"2012/02/12", b"Athens, Greece")

user2.find("photo", 'GreeceProtestTest.jpg')

