from tkinter import filedialog
from PIL import Image
import numpy as np
from Algorithme import Hauteur as ht

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
label = Image.open(path).convert('L')

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
img = Image.open(path).convert('L')

label = np.array(label)
image = np.array(img)

haut = ht.Hauteur(label, image)
print(haut.calcul(300, 550))
