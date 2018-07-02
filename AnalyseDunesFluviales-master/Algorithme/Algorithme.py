from Algorithme import MorphologiquesOperations as mp
from Algorithme import Contraintes as cn
from Algorithme import Operation as ope
from Algorithme import LPE as lpe
from Algorithme import Image as mge
import numpy as np
import cv2
from PIL import Image

#Classe permet de lancer l'algorithme de Ligne de Partage des Eaux de Vincent&Soille et d'obtenir tous les résultats
class RunLPE():
	#Initialise toutes les variables nécessaires
	#@param image : image (liste de liste)
	#@param step : int
	def __init__(self, image, step):
		self.image = np.asmatrix(image).tolist() #Image mis sous forme de liste
		self.imageOrig = self.image #Pour garder l'image originale
		self.hauteurImage = len(image) #Variables pour la hauteur
		self.largeurImage = len(image[0]) #Variables pour la largeur
		self.step = step #Nombre ajouté 

		self.lab = 0

	#Fait le gradient de l'image, fait la contrainte de par contraste dessus, puis applique dessus la LPE
	#apres erosion pour trouver les zones
	def process(self):
		mop = mp.MorphologiquesOperations(False)
		gim = mop.gradient(self.image, 2)
		op = ope.Operation()

		print("Gradient done")

		if(self.step != 0):
			gim = cn.Contraintes().contraste(gim, self.step)

		self.image = gim

		a = np.array(self.image)

		print("Start flooding")

		lp = lpe.LPE(self.image)
		self.lab = lp.runLPE()

	#Permet d'obtenir l'image des labels 
	#@return label : image (liste de liste)
	def getLab(self):
		return self.lab.getImage()

	#Permet d'obtenir l'image des bordures en noir et blanc
	#@return bordure : image (liste de liste)
	def getBordure(self):
		bordure = mge.Image()
		bordure.init2(self.hauteurImage, self.largeurImage)

		for pixel in range(self.lab.getSurface()):
			vallab = self.lab.read2(pixel)
			newvallab = 0
			if(vallab == 0):
				newvallab = 65535
			bordure.write2(pixel, newvallab)
		return bordure.getImage()

	#Permet d'obtenir l'image des bordures sur l'image de base
	#@return image : image (liste de liste)
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


