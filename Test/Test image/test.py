from PIL import Image
import tkinter
from tkinter import filedialog
import cv2 as cv
import numpy as np
import numpngw


path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 

img = cv.imread(path,0)





