﻿from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from scipy import array, shape
from numpy import asmatrix
import numpy as np
from TraitementImage import ImageDune, AlgorithmeImageComplete, ExportTXT
from Algorithme import Hauteur
class ResultatsImage(Frame):  

    def __init__(self, fenetre, origine = None, MonImage = None, separation = None, ImageAffiche = [0], SeuilDetectionDune = 0):
        
        self.MonImage = MonImage
        self.ImageAffichage = ImageAffiche
        self.DetectionDune = SeuilDetectionDune
        self.ImageAAfficher = 0 # variable ne pouvant être une variable locale, sinon l'image n'apparaît pas à l'affichage
        self.seuil = 0
        self.miniature = ImageAffiche
        self.image = 0
        self.separation = separation
        self.origine = origine
        
        # Création d'une sous frame pour placer correctement les divers éléments sur la moitié gauche de la fenêtre
        FrameMenu = Frame(fenetre)
        FrameMenu.pack(side=LEFT, fill = BOTH, expand = 1)

        # Création de nos widgets
        Button(FrameMenu, text='Export des résultats', command = lambda : self.ExportTxt()).pack(side=TOP)

        self.FrameTable = Frame(FrameMenu, height=255, width = 255, bd=1, relief=SUNKEN)
        self.FrameTable.pack(side=TOP, fill = BOTH, expand = 1)
        
        self.Table = ttk.Treeview(self.FrameTable, columns=('Nombre', 'LongOnde', 'HautDune'))
        self.VerticalBarreTable = ttk.Scrollbar(self.FrameTable, orient="vertical", command=self.Table.yview)
        self.Table.configure(yscrollcommand=self.VerticalBarreTable.set)
        
        self.Table['show'] = 'headings' # On n'utilise pas la colonne avec les + (on ne l'affiche pas)
        self.Table.pack(side=LEFT, fill = BOTH, expand = 1)
        self.VerticalBarreTable.pack(side=RIGHT, fill = Y)
        
        self.Table.column('Nombre', width=100, anchor='center')
        self.Table.heading('Nombre', text='Nb Dunes')
        self.Table.column('LongOnde', width=150, anchor='center')
        self.Table.heading('LongOnde', text="Longueur d'onde (m)")
        self.Table.column('HautDune', width=140, anchor='center')
        self.Table.heading('HautDune', text="Hauteur dune (cm)")
        

        img = np.array(MonImage)
        img = Image.fromarray(img)
        self.image = img

        self.Canevas = Canvas(fenetre)
        self.ImageAAfficher = ImageTk.PhotoImage(img)
        self.Canevas.create_image(0,0,anchor=NW,image = self.ImageAAfficher)
        self.Canevas.config(width=img.size[0], height=img.size[1])
        self.Canevas.configure(cursor="crosshair")
        self.Canevas.bind("<Button-1>", self.Hauteur)
        self.Canevas.pack(side=RIGHT, fill = BOTH, expand = 1) 
        
        self.RemplirTableauResultats()
        self.TableauAnalyseImage = [0,0,0,0,0]
        self.BilanDunesImage = [0,0,0]
        

        #AlgorithmeImageComplete.FiltrageLaplacien(MonImage)

    def ExportTxt(self):
        ExportTXT.ExportResultatsDunes(self.TableauAnalyseImage, self.MonImage, self.BilanDunesImage)
    
    def RemplirTableauResultats(self, ResultatsDunes = array([[0,0,0]])):
        NombreDunes = shape(ResultatsDunes)[0]
        for i in range (0, NombreDunes):
            self.Table.insert('', 'end', str(i), text='Axe ' + str(i), values = (str(ResultatsDunes[i][0]), str(ResultatsDunes[i][1]), str(ResultatsDunes[i][2])))

    def Hauteur(self, event):
        PositionX = event.x
        PositionY = event.y
        if(PositionX <  self.image.size[0] and PositionY < self.image.size[1]):
            hauteur = Hauteur.Hauteur(self.separation, self.origine.getImage())
            resolution = self.origine.getResolutionAltitude()
            ht  = hauteur.calcul(PositionY, PositionX, resolution)
            messagebox.showinfo("Hauteur", str(ht) + " cm.")