import numpy as np
import math
from random import randrange
from tkinter import* 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from random import randrange

import script as tst
angle = 0
speed = 20
WIDTH = 500
HEIGHT = 500
X1rec = WIDTH/2 - 20
Y1rec = HEIGHT/2 - 20
X2rec = X1rec + 20
Y2rec = Y1rec + 20
X1Line = 0
Y1Line = 0
X2Line = 0
Y2Line = 0
Name = str()
test = "vh"
button = False


def calculateLinePosition():