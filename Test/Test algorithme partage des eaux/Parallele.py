from threading import Thread

class Parallele(Thread):
	def __init__(self, image, x, y, b):
		Thread.__init__(self)
		self.image = image 
		self.x = x
		self.y = y
		self.bool = b
		self.r = 0

	def run(self):
		im = []
		im.append(self.image[self.x-1][self.y])
		im.append(self.image[self.x+1][self.y])
		im.append(self.image[self.x][self.y])
		im.append(self.image[self.x][self.y-1])
		im.append(self.image[self.x][self.y+1])
		if(self.bool):
			im.append(self.image[self.x-1][self.y-1])
			im.append(self.image[self.x-1][self.y+1])
			im.append(self.image[self.x+1][self.y-1])
			im.append(self.image[self.x+1][self.y+1])
		self.r = min(min(im), 255)

	def join(self):
		return self.r

