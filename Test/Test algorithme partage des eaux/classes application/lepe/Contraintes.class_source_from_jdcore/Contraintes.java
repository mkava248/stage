package lpe;

import java.io.PrintStream;

public class Contraintes
{
  public Contraintes() {}
  
  public static GrayImage parMarqueurs(GrayImage image, GrayImage mask, boolean fourOrEight)
  {
    if ((image.getWidth() != mask.getWidth()) || 
      (image.getHeight() != mask.getHeight())) {
      return null;
    }
    GrayImage maskedImage = Operations.minimun(image, mask);
    
    return eroderGeodesiquement(mask, maskedImage, fourOrEight);
  }
  

  public static GrayImage eroderGeodesiquement(GrayImage ca, GrayImage parRaportAca, boolean fourOrEight)
  {
    if ((ca.getWidth() != parRaportAca.getWidth()) || 
      (ca.getHeight() != parRaportAca.getHeight())) {
      return null;
    }
    GrayImage result = new GrayImage(ca.getHeight(), ca.getWidth());
    
    MorphologicalOperation mop = new MorphologicalOperation(fourOrEight);
    

    GrayImage tmp = ca;
    
    int i = 0;
    do
    {
      result = tmp;
      GrayImage newMask = mop.erode(tmp, 1);
      
      tmp = Operations.maximum(parRaportAca, newMask);
      
      i++;
    } while (!
    





      Operations.equals(result, tmp));
    
    System.out.println("iterations :" + --i);
    
    return result;
  }
  

  public static GrayImage parContrast(GrayImage image, int dynamique, boolean fourOrEight)
  {
    return eroderGeodesiquement(Operations.plus(image, dynamique), image, fourOrEight);
  }
}
