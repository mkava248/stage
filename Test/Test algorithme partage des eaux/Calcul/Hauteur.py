from Algorithme import Pixel as pi

class Hauteur():
	def __init__(self, label, image):
		self.label = label
		self.image = image
		self.hauteur = len(image)
		self.largeur = len(image[0])

	def calcul(self, x, y):
		pile = []
		done = []
		maximum = 0
		minimum = 0
		if(self.label[x][y] != 255):
			maximum = self.image[x][y]
			minimum = self.image[x][y]
			pile.append(pi.Pixel(x, y, 0))
			done.append(pi.Pixel(x, y, 0))

		while(len(pile) != 0):
			pix = pile.pop(0)
			x = pix.getX()
			y = pix.getY()
			for i in range(-1, 2, 1):
				if(x+i < 0 or x+i >= self.hauteur):
					continue
				for j in range(-1, 2, 1):
					if(y+j < 0 or y+j >= self.largeur):
						continue
					pixel = pi.Pixel(x+i, y+j, 0)
					if(self.label[x+i][y+j] != 255 and pixel not in done):
						fifo.append(pi.Pixel(x+i, y+j, 0))
						done.append(pi.Pixel(x+i, y+j, 0))
						maximum = max(maximum, self.image[x+i][y+j])
						minimum = min(minimum, self.image[x+i][y+j])

		hauteur = maximum-minimum
		return hauteur