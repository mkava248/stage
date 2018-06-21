from MorphologiquesOperations import MorphologiquesOperations
from Operation import Operation

class Contraintes():
	def __init__(self):
		self

	def contraste(self, gim, step):
		mop = MorphologiquesOperations(1);
		tmp = Operation().plus(gim, step)
		
		result = tmp[:]
		masque = mop.erode(tmp)
		tmp = Operation().maximum(gim, masque)
		print("First operation")

		i = 1
		while(Operation().egale(result, tmp) == 0):
			result = tmp[:]
			masque = mop.erode(tmp)
			tmp = Operation().maximum(gim, masque)
			print("Operation in work")
			i+=1
		print(i)
		return result