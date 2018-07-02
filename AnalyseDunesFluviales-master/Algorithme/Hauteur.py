from Algorithme import Pixel as pi
from Algorithme import ListPixel as lp
import numpy as np
from PIL import Image

class Hauteur():
	def __init__(self, separation, image):
		self.separation = separation
		self.image = np.asmatrix(image).tolist()
		self.largeur = len(self.image[0])
		self.hauteur = len(self.image)
		print(self.largeur, self.hauteur)
		#print(self.largeur * self.hauteur)
		image = np.array(separation)
		image = Image.fromarray(image)
		image.show()


	def calcul(self, x, y, valeurPixel):
		pile = []
		done = lp.ListPixel()
		maximum = 0
		minimum = 0
		print("Calcul Hauteur")
		if(self.separation[x][y] != 255):
			maximum = self.image[x][y]
			minimum = self.image[x][y]
			pile.append(pi.Pixel(x, y, 0))
			done.addPixel(pi.Pixel(x, y, 0))
		else : 
			print("Pas bon")

		azer = 0
		while(len(pile) != 0):
			#print(azer)
			pix = pile.pop(0)
			x = pix.getX()
			y = pix.getY()
			for i in range(-1, 2, 1):
				if(x+i < 0 or x+i >= self.hauteur):
					continue
				for j in range(-1, 2, 1):
					if(y+j < 0 or y+j >= self.largeur or (i+j)%2 == 0):
						continue
					pixel = pi.Pixel(x+i, y+j, 0)
					if(self.separation[x+i][y+j] != 255 and pixel not in done):
						#print(x+i, y+j)
						pile.append(pixel)
						done.addPixel(pixel)
						maximum = max(maximum, self.image[x+i][y+j])
						minimum = min(minimum, self.image[x+i][y+j])

		maximum = maximum * valeurPixel
		minimum = minimum * valeurPixel
		hauteur = maximum-minimum
		return hauteur #En centimètre
