from PIL import Image
import numpy as np

from Pixel import Pixel
from ListPixel import ListPixel

class Image():
	def __init__(self):
		self.image = [] 
		self.largeur = 0
		self.hauteur =  0
		self.surface = 0 
		self.listPixel = ListPixel()

	def init1(self, image):
		self.image = image
		self.hauteur = len(image)
		self.largeur = len(image[0])
		self.surface = self.largeur * self.hauteur
		self.listPixel.addPixels(self.image)

	def init2(self, h, w):
		self.largeur = w
		self.hauteur = h
		self.surface = w*h
		self.image = np.zeros((h, w)).tolist()

	def init3(self, h, w, value):
		self.largeur = w
		self.hauteur = h
		self.surface = w*h
		self.image = np.full((h,w), value).tolist()

	def read1(self, h, w):
		return self.image[h][w]

	def write1(self, h, w, value):
		self.image[h][w] = value

	def read2(self, p):
		return self.image[int(p/self.largeur)][int(p%self.largeur)]

	def write2(self, p, value):
		self.image[int(p/self.largeur)][int(p%self.largeur)] = value

	def getHeight(self):
		return self.hauteur

	def getWidth(self):
		return self.largeur

	def getSurface(self):
		return self.surface

	def getNumberPixelsAtLevel(self, level):
		return self.listPixel.getNumberOfPixelInLevel(level)

	def getImage(self):
		return self.image

	def getColumnFromAbsolutePosition(self, p):
		return int(p%self.largeur)

	def getRowFromAbsolutePosition(self, p):
		return int(p/self.largeur)

	def getAbsolutePosition(self, row, column):
		return row*self.largeur+column

