#
# HTT Ch 8 code example:
#
# Section 8.11, example 1: pixelex1a
#

import cImage as image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())
