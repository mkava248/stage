from ListPixel import ListPixel
from Pixel import Pixel
from MorphologiquesOperations import MorphologiquesOperations
from Contraintes import Contraintes
from Operation import Operation
from LPE import LPE
import Image as mge
import numpy as np
import cv2
from tkinter import filedialog
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as mppyp

class VincentSoille():
	def __init__(self, image):
		self.INIT = -1 #Valeur du pixel initiale
		self.MASK = -2 #Masque appliquer à un pixel
		self.WSHED = 0 #Valeur quand un pixel est sur la ligne
		self.pFictif = Pixel(-1, -1, -1) #Pixel fictif
		self.actLab = 0 #Actuel label de zone
		self.hMin = 0 #Hauteur minimum
		self.hMax = 255 #Hauteur maximum

		self.image = np.asmatrix(image).tolist() #Image

		self.imageOrig = self.image
		self.largeurImage, self.hauteurImage = image.size #Variables pour la largeur et la hauteur

		self.listFifo = [] #Liste dans laquelle on ajoutera les pixels pour les expensions
		self.listPixel = ListPixel() #Liste comprenant tous les pixels dans

		self.lab = [] #Liste qui permettra de savoir dans quel label sont les pixels
		self.dist = [] #Liste des distances (Voir l'algorithme de Vincent & Soille)
		self.rturn = []

		self.coorX = [-1, 0, 1, 1, 1, 0, -1, -1] #Coordonnées X pour les voisins
		self.coorY = [-1, -1, -1, 0, 1, 1, 1, 0] #Coordonnées Y pour les voisins

		self.step = 0

	def init(self, step):
		self.listPixel.addPixels(self.image)
		#self.listPixel.sortListByLevel()
		self.hMin = self.listPixel.getLevelMin()
		self.hMax = self.listPixel.getLevelMax()

		for x in range(self.hauteurImage):
			self.lab.append([self.INIT]*self.largeurImage)
			self.dist.append([0]*self.largeurImage)
			self.rturn.append([0]*self.largeurImage)

		self.step = step

	def flooding(self):
		curdist = 0
		#Boucle des niveaux
		for h in range(self.hMin, self.hMax+1, 1):
			print(h)
			#Première boucle pour masquer et regarder une première fois les voisins
			pixels = self.listPixel.getPixelsByLevel(h)
			for pixel in pixels : 
				self.lab[pixel.getX()][pixel.getY()] = self.MASK
				self.neighbour(pixel) #Voisin

			curdist = 1
			self.listFifo.append(self.pFictif)

			#Seconde boucle
			while 1:
				pixel = self.listFifo.pop(0)
				if(pixel.getX() == self.pFictif.getX() and pixel.getY() == self.pFictif.getY()):
					if(len(self.listFifo) == 0):
						break
					else:
						self.listFifo.append(self.pFictif)
						curdist += 1
						pixel = self.listFifo.pop(0)

				#Inspection des voisins
				xp = pixel.getX() #Coordonnées du pixel d'origine
				yp = pixel.getY()
				for q in range(8):
					xq = xp + self.coorX[q] #Coordonnées du voisin
					yq = yp + self.coorY[q]
					if(xq < 0 or yq < 0 or xq >= self.hauteurImage or yq >= self.largeurImage):
						continue

					#Si le voisin fait déjà parti d'un  bassin ou est inondé
					if(self.dist[xq][yq] < curdist and ((self.lab[xq][yq] > 0) or self.lab[xq][yq] == self.WSHED)):
						if(self.lab[xq][yq] > 0):
							if(self.lab[xp][yp] == self.MASK or self.lab[xp][yp] == self.WSHED):
								self.lab[xp][yp] = self.lab[xq][yq]
							elif(self.lab[xp][yp] != self.lab[xq][yq]):
								self.lab[xp][yp] = self.WSHED
						elif(self.lab[xp][yp] == self.MASK):
							self.lab[xp][yp] = self.WSHED

					elif(self.lab[xq][yq] == self.MASK and self.dist[xq][yq] == 0):
						self.dist[xq][yq] = curdist + 1
						self.listFifo.append(Pixel(xq, yq, 0))

			#Troisième boucle pour la recherche d'un nouveau niveau minimum
			for pixel in pixels : 
				x = pixel.getX()
				y = pixel.getY()
				self.dist[x][y] = 0 #Réinitialise la distance
				if(self.lab[x][y] == self.MASK):
					self.actLab += 1
					self.listFifo.append(Pixel(x, y, 0))
					self.lab[x][y] = self.actLab
					while(len(self.listFifo) != 0):
						pixel = self.listFifo.pop(0)
						xPixel = pixel.getX() #Coordonnées du pixel d'origine
						yPixel = pixel.getY()
						for k in range(8):
							xk = xPixel + self.coorX[k] #Coordonnées du voisin
							yk = yPixel + self.coorY[k]
							if(xk < 0 or yk < 0 or xk >= self.hauteurImage or yk >= self.largeurImage):
								continue

							if(self.lab[xk][yk] == self.MASK):
								self.listFifo.append(Pixel(xk, yk, 0))
								self.lab[xk][yk] = self.actLab


	def neighbour(self, pixel):
		done = True
		for k in range(8):
			if(done):
				xk = pixel.getX() + self.coorX[k]
				yk = pixel.getY() + self.coorY[k]
				if(xk < 0 or yk < 0 or xk >= self.hauteurImage or yk >= self.largeurImage):
					continue

				if(self.lab[xk][yk] > 0 or self.lab[xk][yk] == self.WSHED):
					self.dist[pixel.getX()][pixel.getY()] = 1
					self.listFifo.append(Pixel(pixel.getX(), pixel.getY(), 0))
					done = False

	def process(self):

    	
		mop = MorphologiquesOperations(0)
		gim = mop.gradient(self.image, 2)
		op = Operation()


		print("Gradient done")

		if(self.step != 0):
			gim = Contraintes().contraste(gim, self.step)

		self.image = gim

		a = np.array(self.image)
		mpimg.imsave("apres erosion.jpg", a, cmap ='gray')

		print("Start flooding")

		lpe = LPE()
		lpe.init(self.image)
		self.lab = lpe.runLPE()

		#self.flooding()


	def getLab(self):
		return self.lab.getImage()
		

	def getReturn(self):
		label = mge.Image()
		label.init2(self.hauteurImage, self.largeurImage)

		for pixel in range(self.lab.getSurface()):
			vallab = self.lab.read2(pixel)
			newvallab = 0
			if(vallab == 0):
				newvallab = 65535
			label.write2(pixel, newvallab)
		return label.getImage()

	def getSepOnImage(self):
		im = mge.Image()
		im.init1(self.imageOrig)
		for pixel in range(self.lab.getSurface()):
			vallab = self.lab.read2(pixel)
			newvallab = im.read2(pixel)
			if(vallab == 0):
				newvallab = 0
			im.write2(pixel, newvallab)
		return im.getImage()


