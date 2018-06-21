from ListPixel import ListPixel
from Pixel import Pixel
from MorphologiquesOperations import MorphologiquesOperations
from Image import Image
import matplotlib.image as mpimg

class LPE():
	def __init__(self):
		self.INIT = -1
		self.MASK = -2
		self.WSHED = 0
		self.MARK = -1

		self.histogramme = [0]*256
		self.image = Image()
		self.sortedImage = Image()
		self.sortedPixels = ListPixel()

		self.pFictif = Pixel(-1, -1, -1)



	def init(self, image):
		self.image.init1(image)
		self.histo()
		print("histo")
		self.sortImage()
		print("sort")

	def histo(self):
		for level in range(256):
			self.histogramme[level] = self.image.getNumberPixelsAtLevel(level)

	def sortImage(self):
		self.sortedPixels.addPixels(self.image.getImage())


	def isNeighbour(self, h, w, row, column, varRow, varCol):
		if((row+varRow>=0) and (row+varRow < h) and (column+varCol>=0) and (column+varCol < w)):
			return ((varRow == 0 and varCol != 0) or (varRow != 0 and varCol == 0))
		return False

	def runLPE(self):
		lab = Image()
		lab.init3(self.image.getHeight(), self.image.getWidth(), -1)
		dist = Image()
		dist.init2(self.image.getHeight(), self.image.getWidth())

		curlab = 0

		pile = []

		for h in range(256):
			print(h)

			pixels = self.sortedPixels.getPixelsByLevel(h)
			for curPix in pixels:
				lab.write1(curPix.getX(), curPix.getY(), -2)
				row = curPix.getX()
				column = curPix.getY()

				done = True
				for varRow in range(-1, 2, 1):
					if(done):
						for varCol in range(-1, 2, 1):
							if (done):
								if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
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

				for varRow in range(-1, 2, 1):
					for varCol in range(-1, 2, 1):
						if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
							neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
							if((dist.read2(neighbourPos)< curDist) and (lab.read2(neighbourPos) > 0 or lab.read2(neighbourPos) == self.WSHED)):
								if(lab.read2(neighbourPos)>0):
									if(lab.read1(curPix.getX(), curPix.getY()) == -2 or lab.read1(curPix.getX(), curPix.getY()) == self.WSHED):
										lab.write1(curPix.getX(), curPix.getY(), lab.read2(neighbourPos))
									elif (lab.read1(curPix.getX(), curPix.getY()) != lab.read2(neighbourPos)):
										lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
										#lab.write2(neighbourPos, curlab)
								elif(lab.read1(curPix.getX(), curPix.getY()) == -2):
									lab.write1(curPix.getX(), curPix.getY(), self.WSHED)
									#lab.write2(neighbourPos, curlab)
							elif(lab.read2(neighbourPos) == -2 and dist.read2(neighbourPos) == 0):
								dist.write2(neighbourPos, curDist+1)
								pile.append(Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
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
						for varRow in range(-1, 2, 1):
							for varCol in range(-1, 2, 1):
								if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row2, column2, varRow, varCol)):
									neighbourPos = lab.getAbsolutePosition(row2+varRow, column2+varCol)
									if(lab.read2(neighbourPos) == -2):
										pile.append(Pixel(self.image.getRowFromAbsolutePosition(neighbourPos),
											self.image.getColumnFromAbsolutePosition(neighbourPos), 0))
										lab.write2(neighbourPos, curlab)

		print("Segmentation")
		if(True):
			for curPix in range(lab.getSurface()):
				if(lab.read2(curPix)>0):
					row = lab.getRowFromAbsolutePosition(curPix)
					column = lab.getColumnFromAbsolutePosition(curPix)

					done = True
					for varRow in range(-1, 2, 1):
						if(done):
							for varCol in range(-1, 2, 1):
								if (done):
									if(self.isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol)):
										neighbourPos = lab.getAbsolutePosition(row+varRow, column+varCol)
										if(lab.read2(curPix) > lab.read2(neighbourPos) and lab.read2(neighbourPos)>0):
											lab.write2(curPix, 0)
											done = False
		return lab
