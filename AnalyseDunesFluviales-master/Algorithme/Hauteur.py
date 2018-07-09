from Algorithme import Pixel as pi
from Algorithme import ListPixel as lp
import numpy as np
from PIL import Image

#Classe pour calculer la hauteur d'une dune
class Hauteur():
	#Initialisation du calcul
	#@param separation (image des bordures) : image (liste de liste)
	#@param image (image originale) : image (liste de liste)
	def __init__(self, separation, image):
		self.separation = separation
		self.image = np.asmatrix(image).tolist()
		self.largeur = len(self.image[0])
		self.hauteur = len(self.image)

	#Calcul de la hauteur
	#@param x : int
	#@param y : int
	#@param valeurPixel : int
	#@return hauteur : int
	def calcul(self, x, y, valeurPixel):
		pile = []
		moyenne = []
		maximum = 0
		minimum = 0
		hauteur = 0
		print("Calcul Hauteur")
		if(self.separation[x][y] != 65535):
			maximum = self.image[x][y]
			minimum = self.image[x][y]
			pile.append(pi.Pixel(x, y, 0))
			self.separation[x][y] = 65535
		else : 
			print("Pas bon")
			return None

		while(len(pile) != 0):
			pix = pile.pop(0)
			x = pix.getX()
			y = pix.getY()
			for i in range(-1, 2, 1):
				if(x+i < 0 or x+i >= self.hauteur):
					continue
				for j in range(-1, 2, 1):
					if(y+j < 0 or y+j >= self.largeur or (i+j)%2 == 0):
						continue
					pixel = pi.Pixel(x+i, y+j, self.image[x+i][y+j])
					if(self.separation[x+i][y+j] != 65535):
						#print(x+i, y+j)
						pile.append(pixel)
						self.separation[x+i][y+j] = 65535
						moyenne.append(self.image[x+i][y+j])
						maximum = max(maximum, self.image[x+i][y+j])
						minimum = min(minimum, self.image[x+i][y+j])

		moy = sum(moyenne)/len(moyenne)	
		print(maximum, minimum)		
		moyCal = moy-minimum
		maximum = maximum * valeurPixel
		minimum = minimum * valeurPixel
		hauteur = maximum-minimum
		print(maximum, minimum)
		return hauteur #En mètre
