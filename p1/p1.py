#Paul Scala
#COP4045
#April 25 2023
#Z23561522
#Homework #6
#Problem 1

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def image_load(filename):
    return plt.imread(filename)


def convert_bw(img):
    # Compute the grayscale version of a color image
    return np.uint8(np.mean(img, axis=2, keepdims=True))

def image_gen(file, steps=30):
    """Generator for image arrays."""
    color_img = image_load(file)     # load the color image
    bw_img = convert_bw(color_img)   # convert the color image to B/W

    # go from color_img to bw_img than back to color_img. s varies from 0 to 1 and then back to 0:
    svalues = np.hstack([np.linspace(0.0, 1.0, steps), np.linspace(1.0, 0, steps)])

    # construct now the list of images, so that we don't have to repeat that later:
    images = [np.uint8(color_img * (1.0 - s) + bw_img * s) for s in svalues]    
    images += [np.uint8(bw_img * (1.0 - s) + color_img * s) for s in svalues]

    # get a  new image as a combination of color_img and bw_img
    while True:             # repeat all images in a loop
        for img in images:
           yield img 
            
fig = plt.figure()
# create image plot and indicate this is animated. Start with an image.
im = plt.imshow(image_load("florida-keys-800-480.jpg"), interpolation='none', animated=True)

# the two images must have the same shape:
imggen = image_gen("florida-keys-800-480.jpg", steps=30)

# updatefig is called for each frame, each update interval:
def updatefig(*args):
    global imggen
    img_array = next(imggen)     # get next image animation frame
    im.set_array(img_array)       # set it. FuncAnimation will display it
    return (im,)

# create animation object that will call function updatefig every 60 ms
ani = animation.FuncAnimation(fig, updatefig, interval=60, blit=False)
plt.title("Color to B/W transition")
plt.show()
