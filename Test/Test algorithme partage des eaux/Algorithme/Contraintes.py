from Algorithme import MorphologiquesOperations as mp
from Algorithme import Operation as OP

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
		mop = mp.MorphologiquesOperations(1);
		tmp = OP.Operation().plus(gim, step)
		
		result = tmp[:]
		masque = mop.erode(tmp)
		tmp = OP.Operation().maximum(gim, masque)
		print("First operation")

		i = 1
		while(OP.Operation().egale(result, tmp) == 0):
			result = tmp[:]
			masque = mop.erode(tmp)
			tmp = OP.Operation().maximum(gim, masque)
			print("Operation in work")
			i+=1
		print(i)
		return result