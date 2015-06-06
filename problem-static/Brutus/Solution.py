#!/usr/bin/python

import hashlib, sys

encrypted_pass = '66ad2dced84182ab686bb60e00fbc7fd'

words = open("words.txt", "r").readlines()

for word in words:
    word = word.strip("\n")
    for number in range(1000, 9999):
        candidate = word + str(number)
        print "Testing %s" %(candidate)
        hashed_candidate = hashlib.md5(candidate).hexdigest()
        if hashed_candidate == encrypted_pass:
            print "The flag is %s" %(candidate)
            sys.exit(0)
