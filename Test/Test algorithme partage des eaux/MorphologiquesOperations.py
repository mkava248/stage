from Operation import Operation
import numpy as np
from Parallele import Parallele
import cv2
import os
import matplotlib.image as mpimg

class MorphologiquesOperations():

	def __init__(self, bool):
		if(bool == 1):
			self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
		else:
			self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))



	def dilate(self, image):
		img = np.array(image, dtype = np.uint8)
		return cv2.dilate(img, self.kernel, iterations = 1)


	def erode(self, image):
		img = np.array(image, dtype = np.uint8)
		return cv2.erode(img,self.kernel,iterations = 1)



	def gradient(self, image, size):
		dil = self.dilate(image)
		ero = self.erode(image)

		print("Dil and ero done")
		i = 1
		while i < size:
			dil = self.dilate(dil)
			ero = self.erode(ero)
			print("Dil and ero done")
			i += 1 
		return Operation().minus(dil, ero)
