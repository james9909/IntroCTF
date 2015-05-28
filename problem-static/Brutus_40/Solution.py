#!/usr/bin/python

import hashlib, sys

encrypted_pass = '147107ad8ee2998634c3c49666baa3a4'
p = "hotspootsalt3617"

words = open("words.txt", "r").readlines()

for word in words:
    word = word.strip("\n")
    for number in range(1000, 5000):
        candidate = 'hotspoot' + word + str(number)
        print "Testing %s" %(candidate)
        hashed_candidate = hashlib.md5(candidate).hexdigest()
        if hashed_candidate == encrypted_pass:
            print "The flag is %s" %(candidate)
            sys.exit(0)
