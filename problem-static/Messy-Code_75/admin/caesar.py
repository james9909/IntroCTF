import sys as f
import string as k

def caesar(ples, dank):
    dog = k.ascii_lowercase
    danked_wut = dog[dank:] + dog[:dank]
    table = k.maketrans(dog, danked_wut)
    return ples.translate(table)

def main(argv):
    if (len(f.argv) != 3):
        print 'pls'
        f.exit(0)

    if caesar(f.argv[1], 15) == caesar("iwtuapvxhgxedqujhrpit", 26):
        print 'ye boi'
    else:
        print 'uw0tm8'

main(f.argv)
