from Algorithme import MorphologiquesOperations as mp
from Algorithme import Operation as OP
import numpy as np

#Classe pour la contrainte
class Contraintes():
	#Initialisation
	def __init__(self):
		pass

	#Contrainte par le contraste
	#@param gim (image apres gradient) : image (liste de liste)
	#@param step (valeur à ajouter pour relever le niveau bas) : int
	#@return result : image (liste de liste)
	def contraste(self, gim, step):
		mop = mp.MorphologiquesOperations(True);
		gim = np.array(gim)
		tmp = OP.Operation().plus(gim, step)
		
		result = tmp[:]
		masque = mop.erode(tmp)
		tmp = OP.Operation().maximum(gim, masque)
		print("First operation")

		i = 1
		while(not OP.Operation().egale(result, tmp)):
			result = tmp[:]
			masque = mop.erode(tmp)
			tmp = OP.Operation().maximum(gim, masque)
			print("Operation in work")
			i+=1
		print(i)
		return result