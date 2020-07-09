#
# HTT Ch 8 code example:
#
# Section 8.11, example 2: pixelex1
#

import cImage as image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())
