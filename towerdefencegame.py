
### import modules ###
import pygame
import random
from random import randint
import Tkinter as tk
from Tkinter import *
from pygame import *
import math
#import datetime
import sys
import time
pygame.init()
######################

### start ###
def start():
    print 'welcome to big bad boy braz tower defence game!'
    print 'press: 1 = map1, s = see your high scores.'
    optiona = raw_input('pick an option: ')
    if optiona == '1':
        execfile('map1.py')
        return
    elif optiona == 's':
        scorefile = open('scores.txt','r')
        for i in scorefile:
            print i
    else:
        start()
def endgame():
    print 'Game over!'
    print 'Your score was:'
    print score
    pygame.quit()
    options = raw_input('Enter your name or type cancel: ')
    if options == 'cancel':
        start()
        return
    else:
        scorefile = open('scores.txt','a')
        scorefile.write(options + "_")
        scorefile.write(str(score) +"\n")
        scorefile.close()
        start()
        return
start()
