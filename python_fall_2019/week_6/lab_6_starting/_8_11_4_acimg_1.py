#
# HTT Ch 8 code example:
#
# Section 8.11, example 4: acimg_1
#

import cImage as image

# img = image.Image("goldygopher.png")
img = image.Image("luther.jpg")
# img = image.Image("cy.png")
print (img.getWidth(),img.getHeight())

win = image.ImageWin(500, 500) # img.getWidth()+200, img.getHeight())
img.draw(win)
# img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)

win.exitonclick()
