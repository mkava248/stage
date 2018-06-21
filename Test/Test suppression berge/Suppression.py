import numpy as np
from PIL import Image
import matplotlib.image as mpimg
from tkinter import filedialog

class sup():
	def __init__(self, image):
		self.largeur, self.hauteur = image.size
		self.image = np.asmatrix(image).tolist()

	def sup(self, haut, bas, gauche, droite):
		img = np.array(self.image)
		i = img == 255

		i = i.tolist()
		for y in range(self.largeur):
			x = 0
			start = False
			while(x < self.hauteur and i[x][y]):
				x += 1
				start = True

			if(start):
				for k in range(haut):
					if(x+k >= self.hauteur):
						continue
					i[x+k][y] = True

			x = self.hauteur-1
			start = False
			while(x >=0 and i[x][y]):
				x -= 1
				start = True

			if(start):
				for k in range(bas):
					if(x-k < 0):
						continue
					i[x-k][y] = True

		for x in range(self.hauteur):
			y = 0
			start = False
			while(y < self.largeur and i[x][y]):
				y += 1
				start = True

			if(start):
				for k in range(gauche):
					if(y+k >= self.largeur):
						continue
					i[x][y+k] = True

			y = self.largeur-1
			start = False
			while(y >=0 and i[x][y]):
				y -= 1
				start = True

			if(start):
				for k in range(droite):
					if(y-k < 0):
						continue
					i[x][y-k] = True

		berge  = np.full((self.hauteur,self.largeur), 255)
		berge = i * berge
		i = np.logical_not(i)
		img = i * img
		img = img + berge
		mpimg.imsave("valeur 0.jpg", img, cmap ='gray')


path = filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')]) 
img = Image.open(path).convert('L')

s = sup(img)
s.sup(10, 10, 10, 10)
