from tkinter import filedialog
import matplotlib.image as mpimg
import cv2
from Algorithme import Algorithme as al
from Suppression import Suppression as sp
from PIL import Image
import numpy as np

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
img = Image.open(path).convert('L')
#img = cv2.imread(path, 0)

suppression = sp.sup(img)
img = suppression.supHautBas(20, 20)

algo = al.RunLPE(img, 0)
print("Init done")
algo.process()
print("Flooding done")
lab = algo.getLab()
bord = algo.getBordure()
img= algo.getSepOnImage()
print("Done")

label = np.array(lab)
bordure = np.array(bord)
image = np.array(img)
print("Process")
mpimg.imsave("label.png", label)
mpimg.imsave("bordures.png", bordure, cmap = 'gray')
mpimg.imsave("bordureSurImage.png", image, cmap = 'gray')
