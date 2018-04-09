"""


"""
import numpy as np

from pyautogui import keyDown, keyUp, screenshot
from random import choice
from time import sleep
from PIL import ImageGrab
from sys import argv
from os import path

key_choices = ['a', 'd']

def hold_key(key):
    print(key)
    keyDown(key)
    sleep(.5)
    keyUp(key)


counter = 0
while True:
    sleep(1)
    playerbox_save_path = path.os.path.dirname(path.realpath(argv[0])) + '/Images/image' + str(counter) + '.jpg'
    playerbox = np.array(ImageGrab.grab(bbox=(530, 310, 825, 460)).save(playerbox_save_path))
    # key = choice(key_choices)
    # hold_key(key)
    counter += 1
