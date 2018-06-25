package gui;

import java.awt.Image;
import java.awt.image.BufferedImage;
import lpe.Contraintes;
import lpe.FactoryLPE;
import lpe.GrayBuffredImage;
import lpe.GrayImage;
import lpe.ImageOperations;
import lpe.MorphologicalOperation;
import lpe.Operations;
















public class GUIMetier
{
  protected Image imageIN;
  protected Image marqueurs;
  protected int tailleFenetre;
  protected int seuil;
  protected int sph1;
  protected int sph2;
  protected int sph3;
  protected boolean filtreMoyenneur;
  protected boolean filtreAlterne;
  protected boolean marqueur;
  protected boolean contraste;
  
  public GUIMetier()
  {
    filtreMoyenneur = false;
    filtreAlterne = false;
    marqueur = false;
    contraste = false;
    sph1 = -1;
    sph2 = -1;
    sph3 = -1;
  }
  
  protected void loadImage(String file) {
    imageIN = FactoryLPE.readImageJPEG(file);
  }
  
  protected void loadMarqueur(String file) {
    marqueurs = FactoryLPE.readImageJPEG(file);
  }
  
  protected void go()
  {
    MorphologicalOperation mop = new MorphologicalOperation(false);
    
    FactoryLPE.viewImage(imageIN, "Image initiale");
    GrayImage gim = FactoryLPE.getGrayImage(imageIN);
    
    GrayImage original = gim;
    




    if (filtreMoyenneur) {
      Image filtre = 
        ImageOperations.simpleMedian(
        FactoryLPE.bufferedImageFromImage(imageIN), 
        tailleFenetre);
      
      gim = FactoryLPE.getGrayImage(filtre);
    }
    


    if ((filtreAlterne) && 
      (sph1 != -1)) {
      gim = mop.OpenClose(gim, sph1);
      if (sph2 != -1) {
        gim = mop.OpenClose(gim, sph2);
        if (sph3 != -1) {
          gim = mop.OpenClose(gim, sph3);
        }
      }
    }
    



    gim = mop.gradient(gim, 2);
    


    if (marqueur)
    {
      FactoryLPE.viewImage(marqueurs, "Image des marqueurs");
      
      GrayImage mask = FactoryLPE.getGrayImage(marqueurs);
      
      mask = Operations.transformerNB(mask);
      
      gim = Contraintes.parMarqueurs(gim, mask, true);
    }
    else if (contraste)
    {
      gim = Contraintes.parContrast(gim, seuil, true);
    }
    



    FactoryLPE factory = new FactoryLPE(new GrayBuffredImage(gim));
    


    BufferedImage bufferedIm = factory.getSeparationOnImage(true, true, imageIN);
    FactoryLPE.viewImage(bufferedIm, "Resultat de la LPE");
    
    bufferedIm = factory.getColorsImage(true, true);
    FactoryLPE.viewImage(bufferedIm, "Resultat de la LPE");
  }
}
