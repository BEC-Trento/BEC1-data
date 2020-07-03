#!/usr/bin/env python
# DMD SCRIPT
#
# Created: 02-2020 CM

"""
A script to generate DMD patterns.
Please, write this script as self-contained as possible,
e.g. avoiding external modules and custom imports
Python is fun!

Available names in the script namespace
----------------------------------------
bec_grid: tuple
    tuple of (X, Y) arrays spanning the coordinates on the atoms' reference frame,
    the scale is micrometers.
    
variables:
    all variables defined in exp_control as dmd_[name] are injected as [name]
    when the script is executed.


Required output
---------------
sequence: list
    the sequence of images for the DMD
"""
import numpy as np

ON = 0  # 2**1 - 1
OFF = 2**8 - 1  # 0
X, Y = bec_grid

def vertical_line(X, Y, x0, width):
    return np.where(abs(X - x0) <= width/2, 1, 0)
    
def angle_line(X, Y, Y0, width, alpha):
    m = np.tan(alpha*np.pi/180)
    return np.where(abs(Y-Y0-m*X)*np.abs(np.cos(alpha*np.pi/180))<= width/2, 1, 0)

# --- start
# get some default values
#x0 = globals().get('x0', 0)
#width = globals().get('width', 10)
#alpha = globals().get('alpha', 45)

im = vertical_line(X, Y, x0, width)
im += angle_line(X, Y, x0, width, alpha)

im = np.where(im, ON, OFF)

sequence = [im]
