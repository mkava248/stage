from PIL import Image
import tkinter
from tkinter import filedialog
import numpy as np
import matplotlib.image as mpimg

class extend():
	def __init__(self):
		self.coordXVoisin = [-1, 0, 1, 1, 1, 0, -1, -1] 
		self.coordYVoisin = [-1, -1, -1, 0, 1, 1, 1, 0]

	def extend(self, img):
		image = img
		imageFinale = []
		i = 0
		while i < len(image):
			imageFinale.append([65536]*len(image[0]))
			i += 1

		x = 0
		while(x < len(image)):
			y = 0
			while(y < len(image[x])):
				for k in range(8):
					xk = x + self.coordXVoisin[k]
					yk = y + self.coordYVoisin[k]

					if(xk < 0 or yk < 0 or xk >= len(image) or yk >= len(image[x])):
						continue

					valeur = image[x][y]
					vk = image[xk][yk]

					if(vk < (valeur/10)):
						imageFinale[x][y] = 0
						continue
				y += 1
			x += 1
		return imageFinale

path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
img = Image.open(path)

e = extend()
ar = e.extend(np.asmatrix(img).tolist())
a = np.array(ar)
print("Finish")
mpimg.imsave("ftr.png", a)
