import numpy, Image

imarray = numpy.random.rand(500,500,3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
im.save('picture.png')
