#!/usr/bin python3

import sys, os
from PIL import Image

if __name__=='__main__':
    myCoolImage = Image.new("RGBA", (690, 420), (52, 146, 235, 123))
    myCoolImage.putpixel((12, 209), (42, 16, 125, 231))
    myCoolImage.putpixel((264, 143), (122, 136, 25, 213))
    exif = myCoolImage.getexif()
    myCoolImage.save("./image.png", "png")

    # ... yeah
    os.system('exiftool -Title="kool_pic" ./image.png')
    os.system('exiftool -Description="jctf{not_the_flag}" ./image.png')
    os.system('exiftool -Author="anon" ./image.png')
