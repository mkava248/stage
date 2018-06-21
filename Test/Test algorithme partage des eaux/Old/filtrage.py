from PIL import Image
import numpy as np
import matplotlib.image as mpimg

class filtre():
	def __init__(self, image):
		self.image = np.asmatrix(image).tolist()
		self.h = len(self.image)
		self.w = len(self.image[0])


	def filtrage(self, step):
		result = np.zeros((self.h, self.w))
		img = np.array(self.image)

		im1 = img == 255
		im1 = im1 * 500
		result = result + im1

		value = 254
		vPixel = 10000
		while value > 0:
			im = img <= value
			im = im * vPixel
			result = result + im
			vPixel += 10000
			value -= step


		return result.tolist()