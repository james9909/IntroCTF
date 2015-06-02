#!/usr/bin/python

from random import *
import sys

choices = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
def rand_string(n):
    string = ""
    for x in range(n):
        string += choice(choices)
    return string

def file_gen():
    name = rand_string(25)
    f = open(name, "w")
    contents = ""
    for x in range(100):
        contents += rand_string(123)
        contents += "\n"
    f.write(contents)

def mass_filegen(num):
    for x in range(num):
        file_gen()

if len(sys.argv) < 2:
    print "Usage: python filegen.py <number of files to generate>"
    sys.exit(0)

mass_filegen(int(sys.argv[1]))
