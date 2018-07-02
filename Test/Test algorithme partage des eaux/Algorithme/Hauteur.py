import Pixel as pi
import ListPixel as lp

class Hauteur():
	def __init__(self, label, image):
		self.label = label
		self.image = image
		self.hauteur = len(image)
		self.largeur = len(image[0])

	def calcul(self, x, y, valeurPixel):
		pile = []
		done = lp.ListPixel()
		maximum = 0
		minimum = 0
		print(self.label[x][y])
		if(self.label[x][y] != 30):
			maximum = self.image[x][y]
			minimum = self.image[x][y]
			pile.append(pi.Pixel(x, y, 0))
			done.addPixel(pi.Pixel(x, y, 0))

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
					pixel = pi.Pixel(x+i, y+j, 0)
					if(self.label[x+i][y+j] != 30 and pixel not in done):
						pile.append(pixel)
						done.addPixel(pixel)
						maximum = max(maximum, self.image[x+i][y+j])
						minimum = min(minimum, self.image[x+i][y+j])

		print(maximum, minimum)
		maximum = maximum * valeurPixel
		minimum = minimum * valeurPixel
		hauteur = maximum-minimum
		return hauteur #En mètre

from tkinter import filedialog
from PIL import Image
import numpy as np
from os.path import basename

path = filedialog.askopenfilename(title="Ouvrir une label",filetypes=[('all files','.*')]) 
label = Image.open(path).convert('L')

path = filedialog.askopenfilename(title="Ouvrir une origine",filetypes=[('all files','.*')]) 
img = Image.open(path).convert('L')

label = np.array(label)
image = np.array(img)

print(basename(path))
NomImage = (path.split("/"))[-1]
DecoupeNomImage = NomImage.split("_")
AltitudeMin = float(DecoupeNomImage[-2].replace(',', '.'))
AltitudeMaximum = float((DecoupeNomImage[-1].split("."))[0].replace(',', '.'))

print(AltitudeMaximum, AltitudeMin)
ResolutionAltitude = round((AltitudeMaximum - AltitudeMin) / 255, 5)
print(ResolutionAltitude)


haut = Hauteur(label, image)
print(haut.calcul(319, 446,ResolutionAltitude))
