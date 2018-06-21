from Pixel import Pixel

class ListPixel():
	def __init__(self):
		self.listPixel = []
		self.number = 0
		for i in range(256):
			self.listPixel.append([])

	def addPixel(self, pixel):
		self.number += 1
		self.listPixel[pixel.getLevel()].append(pixel)

	def addPixels(self, pixels):
		x = 0
		while(x < len(pixels)):
			y = 0 
			while(y < len(pixels[x])):
				self.addPixel(Pixel(x, y, pixels[x][y]))
				y += 1
			x += 1

	def sortListByLevel(self):
		self.listPixel = sorted(self.listPixel, key=lambda pixel: pixel.getLevel())

	def displayList(self):
		for pixels in self.listPixel:
			for pixel in pixels:
				print(pixel.getX(), pixel.getY(), pixel.getLevel())

	def getNumberOfPixelInLevel(self, level):
		return len(self.listPixel[level])

	def getPixelsByLevel(self, level):
		return self.listPixel[level]

	def getLevelMin(self):
		for i in range(256):
			if(len(self.listPixel[i]) != 0):
				return i

	def getLevelMax(self):
		for i in range(255, 0, -1):
			if(len(self.listPixel[i]) != 0):
				return i

	def getNumberPixels(self):
		return self.number
			

#listpixel = ListPixel()
#pixel = Pixel(1,1,1)
#listpixel.addPixel(pixel)
#pixel = Pixel(1,0,0)
#listpixel.addPixel(pixel)
#pixel = Pixel(1,2,1)
#listpixel.addPixel(pixel)
#pixel = Pixel(1,4,1)
#listpixel.addPixel(pixel)
#pixel = Pixel(1,5,2)
#listpixel.addPixel(pixel)

#listpixel.displayList()
#print("-----------------")
#listpixel.sortListByLevel()

#hmin = listpixel.getLevelMin()
#hmax = listpixel.getLevelMax()
#print(hmin, hmax)
#listpixel.displayList()

#gg = listpixel.getPixelsByLevel(1, 4, 1)

#print(listpixel.getNumberOfPixelInLevel(1))
