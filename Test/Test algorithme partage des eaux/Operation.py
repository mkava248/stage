import numpy as np

class Operation():
	def __init__(self):
		self

	def minus(self, im1, im2):
		i1 = np.array(im1)
		i2 = np.array(im2)
		im = i1 - i2
		i = im > 0
		im = im * i
		return im.tolist()


	def plus(self, image, h):
		i = np.array(image)
		i = i+h
		return i.tolist()


	def maximum(self, im1, im2):
		i1 = np.array(im1)
		i2 = np.array(im2)

		i = i1>i2 
		i1 = i1 * i
		i = i2>=i1
		i2 = i2 * i
		iS =i1 +i2
		return iS.tolist()


	def egale(self, im1, im2):		
		if(im1 == im2):
			return 1
		return 0