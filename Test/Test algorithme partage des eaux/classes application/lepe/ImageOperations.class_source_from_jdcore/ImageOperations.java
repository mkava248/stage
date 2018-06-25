package lpe;

import java.awt.image.BufferedImage;
import java.awt.image.ConvolveOp;
import java.awt.image.Kernel;



public class ImageOperations
{
  public ImageOperations() {}
  
  public static BufferedImage simpleMoyenneur(BufferedImage image)
  {
    Kernel k = 
      new Kernel(
      3, 
      3, 
      new float[] {
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F, 
      0.1111F });
    ConvolveOp op = new ConvolveOp(k);
    BufferedImage blurry = op.filter(image, null);
    return blurry;
  }
  
  public static BufferedImage simpleMedian(BufferedImage image, int size)
  {
    int surface = size * size;
    
    float weight = 1.0F / surface;
    
    float[] elements = new float[surface];
    
    for (int i = 0; i < surface; i++) {
      elements[i] = weight;
    }
    
    Kernel k = new Kernel(size, size, elements);
    
    ConvolveOp op = new ConvolveOp(k, 1, null);
    BufferedImage blurry = op.filter(image, null);
    return blurry;
  }
}
