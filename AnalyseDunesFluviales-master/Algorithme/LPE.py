from Algorithme import ListPixel as lp
from Algorithme import Pixel as pi
from Algorithme import Image as mge
import time

#Classe d'algorithme
class LPE():
	#Initialise les données pour la l'algorithme
	def __init__(self, image):
		self.temps = time.clock()
		self.INIT = -1
		self.MASK = -2
		self.WSHED = 0
		self.MARK = -1

		self.image = mge.Image()
		self.image.init1(image)

		self.sortedPixels = lp.ListPixel()
		self.sortedPixels.addPixels(self.image.getImage())
		self.bordure = mge.Image()
		self.bordure.init1(image)
		self.bordure1 = mge.Image()
		self.bordure1.init1(image)

		self.niveau = mge.Image()
		self.niveau.init3(self.image.getHeight(), self.image.getWidth(), -1)
		self.niveau1 = mge.Image()
		self.niveau1.init3(self.image.getHeight(), self.image.getWidth(), -1)

		self.pFictif = pi.Pixel(-1, -1, -1)		

	#Pour savoir si le pixel a des voisins
	#@param h (hauteur de l'image) : int
	#@param w (largeur de l'image) : int
	#@param row (ligne du pixel) : int
	#@param column (colonne du pixel) : int
	#@param varRow (ligne du voisin) : int
	#@param varCol (colonne du voisin) : int
	#@return boolean
	def isNeighbour(self, h, w, row, column, varRow, varCol):
		if((row+varRow>=0) and (row+varRow < h) and (column+varCol>=0) and (column+varCol < w)):
			return ((varRow == 0 and varCol != 0) or (varRow != 0 and varCol == 0))
		return False

	def runLPE(self):
		lab, separation = self.minToMax()
		lab1, separation1 = self.maxToMin()
		return lab, separation, self.bordure, self.niveau, lab1, separation1, self.bordure1, self.niveau1



	#Méthode faisant l'algorithme de Vincent&Soille
	def minToMax(self):
		lab = mge.Image() #Image dans lequel on précise la valeur du label de chaque pixel
		lab.init3(self.image.getHeight(), self.image.getWidth(), -1) #On initialise cette image à -1
		dist = mge.Image() #Image de distance 
		dist.init2(self.image.getHeight(), self.image.getWidth()) #Initialisé à 0
		separation = mge.Image()
		separation.init2(self.image.getHeight(), self.image.getWidth())

		curlab = 0 #Valeur du label actuel

		pile = [] #Pile dans laquelle on va ajouté les pixels à traiter

		#Boucle pour chaque niveaux de gris
		for h in range(256):
			print(h)

			pixels = self.sortedPixels.getPixelsByLevel(h) #Obtenir tous les pixels qui ont la valeur qui sont au self.niveau de gris
			for curPix in pixels:
				lab.write1(curPix.getX(), curPix.getY(), -2)
				row = curPix.getX()
				column = curPix.getY()

				#On regarde si les voisins sont corrects 
				done = True

				for i in range(9):
					varRow = round(i/3-1)
					varCol = round(i%3-1)
					if(varRow>1):
						varRow = -1
					if(done and self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
						if(lab.read1(varRow+row, varCol+column) > 0 or lab.read1(varRow+row, varCol+column) == self.WSHED):
							done = False
							dist.write1(curPix.getX(), curPix.getY(), 1)
							pile.append(curPix)
			curDist = 1
			pile.append(self.pFictif)

			while 1:
				curPix = pile.pop(0)
				if(curPix.getX() == -1 and curPix.getY() == -1):
					if(len(pile) == 0):
						break
					pile.append(self.pFictif)
					curDist += 1
					curPix = pile.pop(0)

				row = curPix.getX()
				column = curPix.getY()

				for i in range(9):
					varRow = round(i/3-1)
					varCol = round(i%3-1)
					if(varRow>1):
						varRow = -1
					if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
						neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
						if((dist.read2(neighbourPos)< curDist) and (lab.read2(neighbourPos) > 0 or lab.read2(neighbourPos) == self.WSHED)):
							if(lab.read2(neighbourPos)>0):
								if(lab.read1(curPix.getX(), curPix.getY()) == -2 or lab.read1(curPix.getX(), curPix.getY()) == self.WSHED):
									lab.write1(curPix.getX(), curPix.getY(), lab.read2(neighbourPos))
								elif (lab.read1(curPix.getX(), curPix.getY()) != lab.read2(neighbourPos)):
									lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
									separation.write1(curPix.getX(), curPix.getY(), 65535)
									self.niveau.write1(curPix.getX(), curPix.getY(), h)
							elif(lab.read1(curPix.getX(), curPix.getY()) == -2):
								lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
								separation.write1(curPix.getX(), curPix.getY(), 65535)
								self.niveau.write1(curPix.getX(), curPix.getY(), h)
						elif(lab.read2(neighbourPos) == -2 and dist.read2(neighbourPos) == 0):
							dist.write2(neighbourPos, curDist+1)
							pile.append(pi.Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
							 self.image.getColumnFromAbsolutePosition(neighbourPos), 0))

			for curPix in pixels:
				dist.write1(curPix.getX(), curPix.getY(), 0)
				if(lab.read1(curPix.getX(), curPix.getY()) == -2):
					curlab += 1
					pile.append(curPix)
					lab.write1(curPix.getX(), curPix.getY(), curlab)
					while(len(pile) != 0):
						curPix = pile.pop(0)
						row2 = curPix.getX()
						column2 = curPix.getY()
						for i in range(9):
							varRow = round(i/3-1)
							varCol = round(i%3-1)
							if(varRow>1):
								varRow = -1
							if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row2, column2, varRow, varCol)):
								neighbourPos = lab.getAbsolutePosition(row2+varRow, column2+varCol)
								if(lab.read2(neighbourPos) == -2):
									pile.append(pi.Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
										self.image.getColumnFromAbsolutePosition(neighbourPos), 0))
									lab.write2(neighbourPos, curlab)

		print("Segmentation")
		for curPix in range(lab.getSurface()):
			if(lab.read2(curPix)>0):
				row = lab.getRowFromAbsolutePosition(curPix)
				column = lab.getColumnFromAbsolutePosition(curPix)
				
				while(True):
					for i in range(9):
						varRow = round(i/3-1)
						varCol = round(i%3-1)
						if(varRow>1):
							varRow = -1
						if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
							neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
							if(lab.read2(curPix) > lab.read2(neighbourPos) and lab.read2(neighbourPos)>0):
								lab.write2(curPix, 0)
								separation.write2(curPix, 65535)
								self.bordure.write2(curPix, 0)
								if(self.niveau.read2(curPix) == -1):
									v = self.getValueLevel(curPix)
									if(v != None):
										#print(v)
										self.niveau.write2(curPix, v)
								break
					break
		
		print(time.clock() - self.temps)
		return lab, separation

	def maxToMin(self):
		lab = mge.Image() #Image dans lequel on précise la valeur du label de chaque pixel
		lab.init3(self.image.getHeight(), self.image.getWidth(), -1) #On initialise cette image à -1
		dist = mge.Image() #Image de distance 
		dist.init2(self.image.getHeight(), self.image.getWidth()) #Initialisé à 0
		separation = mge.Image()
		separation.init2(self.image.getHeight(), self.image.getWidth())

		curlab = 0 #Valeur du label actuel

		pile = [] #Pile dans laquelle on va ajouté les pixels à traiter

		#Boucle pour chaque niveaux de gris
		for h in range(255, 0, -1):
			print(h)

			pixels = self.sortedPixels.getPixelsByLevel(h) #Obtenir tous les pixels qui ont la valeur qui sont au self.niveau de gris
			for curPix in pixels:
				lab.write1(curPix.getX(), curPix.getY(), -2)
				row = curPix.getX()
				column = curPix.getY()

				#On regarde si les voisins sont corrects 
				done = True

				for i in range(9):
					varRow = round(i/3-1)
					varCol = round(i%3-1)
					if(varRow>1):
						varRow = -1
					if(done and self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
						if(lab.read1(varRow+row, varCol+column) > 0 or lab.read1(varRow+row, varCol+column) == self.WSHED):
							done = False
							dist.write1(curPix.getX(), curPix.getY(), 1)
							pile.append(curPix)
			curDist = 1
			pile.append(self.pFictif)

			while 1:
				curPix = pile.pop(0)
				if(curPix.getX() == -1 and curPix.getY() == -1):
					if(len(pile) == 0):
						break
					pile.append(self.pFictif)
					curDist += 1
					curPix = pile.pop(0)

				row = curPix.getX()
				column = curPix.getY()

				for i in range(9):
					varRow = round(i/3-1)
					varCol = round(i%3-1)
					if(varRow>1):
						varRow = -1
					if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
						neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
						if((dist.read2(neighbourPos)< curDist) and (lab.read2(neighbourPos) > 0 or lab.read2(neighbourPos) == self.WSHED)):
							if(lab.read2(neighbourPos)>0):
								if(lab.read1(curPix.getX(), curPix.getY()) == -2 or lab.read1(curPix.getX(), curPix.getY()) == self.WSHED):
									lab.write1(curPix.getX(), curPix.getY(), lab.read2(neighbourPos))
								elif (lab.read1(curPix.getX(), curPix.getY()) != lab.read2(neighbourPos)):
									lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
									separation.write1(curPix.getX(), curPix.getY(), 65535)
									self.niveau.write1(curPix.getX(), curPix.getY(), h)
							elif(lab.read1(curPix.getX(), curPix.getY()) == -2):
								lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
								separation.write1(curPix.getX(), curPix.getY(), 65535)
								self.niveau.write1(curPix.getX(), curPix.getY(), h)
						elif(lab.read2(neighbourPos) == -2 and dist.read2(neighbourPos) == 0):
							dist.write2(neighbourPos, curDist+1)
							pile.append(pi.Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
							 self.image.getColumnFromAbsolutePosition(neighbourPos), 0))

			for curPix in pixels:
				dist.write1(curPix.getX(), curPix.getY(), 0)
				if(lab.read1(curPix.getX(), curPix.getY()) == -2):
					curlab += 1
					pile.append(curPix)
					lab.write1(curPix.getX(), curPix.getY(), curlab)
					while(len(pile) != 0):
						curPix = pile.pop(0)
						row2 = curPix.getX()
						column2 = curPix.getY()
						for i in range(9):
							varRow = round(i/3-1)
							varCol = round(i%3-1)
							if(varRow>1):
								varRow = -1
							if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row2, column2, varRow, varCol)):
								neighbourPos = lab.getAbsolutePosition(row2+varRow, column2+varCol)
								if(lab.read2(neighbourPos) == -2):
									pile.append(pi.Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
										self.image.getColumnFromAbsolutePosition(neighbourPos), 0))
									lab.write2(neighbourPos, curlab)

		print("Segmentation")
		for curPix in range(lab.getSurface()):
			if(lab.read2(curPix)>0):
				row = lab.getRowFromAbsolutePosition(curPix)
				column = lab.getColumnFromAbsolutePosition(curPix)
				
				while(True):
					for i in range(9):
						varRow = round(i/3-1)
						varCol = round(i%3-1)
						if(varRow>1):
							varRow = -1
						if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
							neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
							if(lab.read2(curPix) > lab.read2(neighbourPos) and lab.read2(neighbourPos)>0):
								lab.write2(curPix, 0)
								separation.write2(curPix, 65535)
								self.bordure.write2(curPix, 0)
								if(self.niveau.read2(curPix) == -1):
									v = self.getValueLevel(curPix)
									if(v != None):
										#print(v)
										self.niveau.write2(curPix, v)
								break
					break
		
		print(time.clock() - self.temps)
		return lab, separation


	def getValueLevel(self, pixel):
		row = self.niveau.getRowFromAbsolutePosition(pixel)
		column = self.niveau.getColumnFromAbsolutePosition(pixel)
		for i in range(9):
			varRow = round(i/3-1)
			varCol = round(i%3-1)
			if(varRow>1):
				varRow = -1
			if(self.isNeighbour(self.niveau.getHeight(), self.niveau.getWidth(), row, column, varRow, varCol)):
				if(self.niveau.read1(row+varRow, column+varCol) != -1):
					return self.niveau.read1(row+varRow, column+varCol)
		return None

