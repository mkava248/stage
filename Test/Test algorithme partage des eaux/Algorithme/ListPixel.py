from Algorithme import Pixel as pi

class ListPixel():
	#Initialise les pixels
	def __init__(self):
		self.listPixel = [] #Liste ou le spixels seront rangé par leur valeur
		self.number = 0
		for i in range(256):
			self.listPixel.append([])

	#Ajoute un pixel à la liste
	#@param pixel : Pixel
	def addPixel(self, pixel):
		self.number += 1
		self.listPixel[pixel.getLevel()].append(pixel)

	#Ajoute une liste de pixels
	#@param pixels : image (liste de liste)
	def addPixels(self, pixels):
		x = 0
		while(x < len(pixels)):
			y = 0 
			while(y < len(pixels[x])):
				self.addPixel(pi.Pixel(x, y, pixels[x][y]))
				y += 1
			x += 1

	#Permet d'afficher tous les  pixels de la liste
	def displayList(self):
		for pixels in self.listPixel:
			for pixel in pixels:
				print(pixel.getX(), pixel.getY(), pixel.getLevel())

	#Permet de savoir le nombre de pixels qui sont à un niveau
	#@param level : int 
	#@return taille : int
	def getNumberOfPixelInLevel(self, level):
		return len(self.listPixel[level])

	#Permet d'obtenir tous les pixels appartenant à un niveau
	#@param level : int
	#@return liste de Pixels 
	def getPixelsByLevel(self, level):
		return self.listPixel[level]

	#Permet de savoir le niveau minimum de la liste
	#@return level min : int
	def getLevelMin(self):
		for i in range(256):
			if(len(self.listPixel[i]) != 0):
				return i

	#Permet de savoir le niveau max de la liste
	#@return level max : int
	def getLevelMax(self):
		for i in range(255, 0, -1):
			if(len(self.listPixel[i]) != 0):
				return i

	#Permet de savoir le nombre de pixels dans la liste
	#@return nombre : int
	def getNumberPixels(self):
		return self.number

	#Permet de savoir si un pixel est dans la liste
	#@param pixel : pixel
	def isIn(self, pixel):
		if(pixel in self.listPixel[pixel.getLevel()]):
			return True
		return False

	#Permet de surcharger l'opérateur "in"
	#@param objet : pixel 
	def __contains__(self, objet):
		for pixel in self.listPixel[objet.getLevel()]:
			if(pixel == objet):
				return True
		return False