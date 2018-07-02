class coupure():
	def __init__(self):
		self.x = -1
		self.y = -1
		self.bX = False
		self.bY = False

	def setValues(self, x, y):
		self.x = x
		self.y = y
		self.bX = True
		self.bY = True
		
	def coordonnees(self, x, y):
		if(self.bX == False and self.bY == False):
			self.setValues(x, y)
			return x, y

		Xi = x-self.x
		Yi = y-self.y
		if(abs(Xi)>abs(Yi)):
			if(self.bX):
				self.bX = False
				self.x += Xi
			elif(self.bY):
				self.bY = False
				self.y += Yi
		else:
			if(self.bY):
				self.bY = False
				self.y += Yi
			elif(self.bX):
				self.bX = False
				self.x += Xi

		return self.x, self.y