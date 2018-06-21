import numpy as np
import cv2 as cv
from tkinter import filedialog
from PIL import Image
import matplotlib.image as mpimg

from filtrage import filtre

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')])
img = Image.open(path)

f = filtre(img)
result = f.filtrage(10)
ar = np.array(result)
mpimg.imsave("testoulle.jpg", ar, cmap = 'gray')


