#!/usr/bin/python

import hashlib

encrypted_pass = "5a42277ce25e430dc98f7bd4323e4e7f"

words = open("/etc/dictionaries-common/words", "r").readlines()

for word in words:
    word = word.strip("\n")
    candidate = 'hotspoot' + word
    hashed_candidate = hashlib.md5(candidate).hexdigest()
    if hashed_candidate == encrypted_pass:
        print "The flag is %s" %(candidate)
        break
