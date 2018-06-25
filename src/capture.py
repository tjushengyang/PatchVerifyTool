#!/usr/bin/python3
# -*- coding:utf-8 -*-  
from PIL import ImageGrab
if __name__ == '__main__':
    im = ImageGrab.grab()
    im.save('d:\\12.png')