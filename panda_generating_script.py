from PIL import Image
# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# tells how many times to iterate through the following mechanism
# which equals the number of pandas
# e.g. 
# for x in range(0-200) 
# would generate 201 pandas numbered 0-200
for x in range(0, 50):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    #head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    
    #body color - randomly generate each number in an RGB color
    bc = (randint(0, 256), randint(0, 256), randint(0, 256))
    c=randint(0,500)
    seed(c)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if c > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
        ey = (154, 0, 0)
    e = randint(0,1000)
    seed(e)

    # background
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey background
        bg = (152, 152, 152)
    elif 500 >= f > 47:
        # 48-500 >> gold background
        bg = (204, 172, 0)
    elif 47 >= f > 7:
        # 8 >> 47 >> red background
        bg = (204, 0, 0) 
    else:
        # random number is 7 or less >> black background
        bg = (0, 0, 0) 

    # background color
    #bg = (238, 238, 238)
    # outline color
    ol = (0, 0, 0)

    basic_panda = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg],
        [bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg],
        [bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg],
        [bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg],
        [bg, bg, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg],
        [bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, bg, bg],
        [bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, bg, bg],
        [bg, bg, bg, ol, ol, ol, hd, hd, hd, ew, ew, ew, ew, hd, hd, hd, hd, hd, hd, hd, ew, ew, ew, ew, hd, hd, hd, ol, ol, ol, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, hd, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, ew, ew, ew, ew, hd, ew, ew, hd, hd, hd, hd, hd, ew, ew, hd, ew, ew, ew, ew, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, hd, hd, hd, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, ol, ol, ol, hd, hd, ew, ew, ew, ew, ew, ew, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, ew, ew, ew, ew, ew, hd, hd, ol, ol, ol, ol, ol, hd, hd, ew, ew, ew, ew, ew, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, ew, hd, hd, hd, hd, ol, ol, ol, hd, hd, hd, hd, ew, ew, ew, hd, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bc, bc, bc, bc, bc, bc, bc, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, ol, ol, ol, bc, bc, bc, bc, bc, bc, bc, ol, ol, ol, bc, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    # choose which panda image to use
    seed(f)
    g = randint(251,1000)
    g = 251

    if g > 250:
        # if random number is 251 - 1000 >> basic panda
        pixels = basic_panda
        p = "basic"


    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/panda_images/' + (str(x)) + '.png'
    new_image.save(imgname)
