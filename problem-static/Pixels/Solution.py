from PIL import Image
import hashlib

def is_even(n):
    return n % 2 == 0

def pixels(picture):
    r_all = 0
    b_all = 0
    g_all = 0
    r_even = 0
    b_even = 0
    g_even = 0
    r_odd = 0
    b_odd = 0
    g_odd = 0
    im = Image.open(picture, "r")
    pix = im.load()
    for y in range(500):
        for x in range(500):
            pixels = pix[x, y]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r_all += r
            g_all += g
            b_all += b

            if is_even(x):
                r_even += r
                b_even += b
                g_even += g
            if not is_even(y):
                r_odd += r
                b_odd += b
                g_odd += g

    all_hash = hashlib.md5(str(r_all + g_all + b_all)).hexdigest()
    even_hash = hashlib.md5(strr_even + g_even + b_even).hexdigest()
    odd_hash = hashlib.md5(str(r_odd + g_odd + b_odd)).hexdigest()

    return hashlib.md5(all_hash + even_hash + odd_hash).hexdigest()

print pixels("pixels.png")
