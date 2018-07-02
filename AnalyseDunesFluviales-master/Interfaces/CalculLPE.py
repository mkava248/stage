from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
from numpy import asmatrix
from Algorithme import Algorithme, Suppression
from Interfaces import ResultatsImage

class CalculLPE(Frame):
	def __init__(self, fenetre, MonImage, ImageAffiche, seuilDetection, bCoupure):
		self.monImage = MonImage
		self.miniature = ImageAffiche
		self.seuilDetection = seuilDetection
		self.b = bCoupure

		FrameMenu = Frame(fenetre)
		FrameMenu.pack(side=LEFT, fill = BOTH, expand = 1)
		
		FrameInfoImage = Frame(FrameMenu)
		FrameInfoImage.pack(side=TOP)
		Label(FrameInfoImage, text="Seuil : ").grid(row=0, column=0)
		self.saisi = Entry(FrameInfoImage, width=10)
		self.saisi.grid(row=0, column=1, sticky='ew')
		self.saisi.insert(0, "0")

		Label(FrameInfoImage, text="Haut : ").grid(row=1, column=0)
		self.haut = Entry(FrameInfoImage, width=10)
		self.haut.grid(row=1, column=1, sticky='ew')
		self.haut.insert(0, "0")

		Label(FrameInfoImage, text="Bas : ").grid(row=2, column=0)
		self.bas = Entry(FrameInfoImage, width=10)
		self.bas.grid(row=2, column=1, sticky='ew')
		self.bas.insert(0, "0")

		Label(FrameInfoImage, text="Gauche : ").grid(row=3, column=0)
		self.gauche = Entry(FrameInfoImage, width=10)
		self.gauche.grid(row=3, column=1, sticky='ew')
		self.gauche.insert(0, "0")

		Label(FrameInfoImage, text="Droite : ").grid(row=4, column=0)
		self.droite = Entry(FrameInfoImage, width=10)
		self.droite.grid(row=4, column=1, sticky='ew')
		self.droite.insert(0, "0")
		Button(FrameMenu, text='Calcul de la LPE', 
			command = lambda : self.LPE(MonImage)).pack(side=TOP)

		if(bCoupure):
			self.haut['state'] = 'disabled'
			self.bas['state'] = 'disabled'
			self.gauche['state'] = 'disabled'
			self.droite['state'] = 'disabled'
	
	def LPE(self, monImage):
		seuil = int(self.saisi.get())
		haut = int(self.haut.get())
		bas = int(self.bas.get())
		gauche = int(self.gauche.get())
		droite = int(self.droite.get())

		image = monImage.getImage()

		sp = Suppression.sup(image)
		img = sp.suppression(haut, bas, gauche, droite)
		print("Sup done")

		al = Algorithme.RunLPE(img, seuil)
		al.process()
		print("Process done")

		resultat = al.getSepOnImage()
		bordure = al.getBordure()
		print("Resultat done")
		fenTraitementImage = Toplevel()
		if(self.b):
			fenTraitementImage.title("Résultat coupure image - Analyse dunes 2018")
		else:
			fenTraitementImage.title("Résultats image complète - Analyse dunes 2018")
		ResultatsImage.ResultatsImage(fenTraitementImage, monImage, resultat, bordure, self.miniature, self.seuilDetection)