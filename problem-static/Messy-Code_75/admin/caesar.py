import sys, string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def main(argv):
    if (len(sys.argv) != 3):
        print 'Not enough arguments!'
        sys.exit(0)

    if caesar(sys.argv[1], 15) == "iwtuapvxhgxedqujhrpit":
        print 'Congrats, you got the flag!'
    else:
        print 'Incorrect!'

main(sys.argv)
