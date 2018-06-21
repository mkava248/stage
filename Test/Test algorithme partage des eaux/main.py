from tkinter import filedialog
import matplotlib.image as mpimg
import cv2
from VincentSoille import VincentSoille
from PIL import Image
import numpy as np

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
img = Image.open(path).convert('L')
#img = cv2.imread(path, 0)

vs = VincentSoille(img)
vs.init(8)
print("Init done")
vs.process()
print("Flooding done")
lab = vs.getLab()
bordure = vs.getReturn()
image = vs.getSepOnImage()
print("Done")

a = np.array(lab)
ar = np.array(bordure)
i = np.array(image)
print("Process")
mpimg.imsave("vincentetsoille.png", a)
mpimg.imsave("vincentetsoilleBordure.png", ar, cmap = 'gray')
mpimg.imsave("bordureSurImage.png", i, cmap = 'gray')
