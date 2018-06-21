package lpe;


public class Operations
{
  public Operations() {}
  

  public static GrayImage minimun(GrayImage im1, GrayImage im2)
  {
    if ((im1.getWidth() != im2.getWidth()) || 
      (im1.getHeight() != im2.getHeight())) {
      return null;
    }
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      if (im1.read(i) < im2.read(i)) {
        result.write(i, im1.read(i));
      } else {
        result.write(i, im2.read(i));
      }
    }
    return result;
  }
  
  public static GrayImage maximum(GrayImage im1, GrayImage im2)
  {
    if ((im1.getWidth() != im2.getWidth()) || 
      (im1.getHeight() != im2.getHeight())) {
      return null;
    }
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      if (im1.read(i) > im2.read(i)) {
        result.write(i, im1.read(i));
      } else {
        result.write(i, im2.read(i));
      }
    }
    return result;
  }
  
  public static GrayImage minus(GrayImage im1, GrayImage im2)
  {
    if ((im1.getWidth() != im2.getWidth()) || 
      (im1.getHeight() != im2.getHeight())) {
      return null;
    }
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      int val = im1.read(i) - im2.read(i);
      if (val < 0) val = 0;
      result.write(i, val);
    }
    
    return result;
  }
  
  public static GrayImage plus(GrayImage im1, GrayImage im2)
  {
    if ((im1.getWidth() != im2.getWidth()) || 
      (im1.getHeight() != im2.getHeight())) {
      return null;
    }
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      int val = im1.read(i) + im2.read(i);
      if (val > 255) val = 255;
      result.write(i, val);
    }
    
    return result;
  }
  
  public static boolean equals(GrayImage im1, GrayImage im2)
  {
    if ((im1.getWidth() != im2.getWidth()) || 
      (im1.getHeight() != im2.getHeight())) {
      return false;
    }
    for (int i = 0; i < im2.getSurface(); i++) {
      if (im1.read(i) != im2.read(i)) { return false;
      }
    }
    return true;
  }
  
  public static GrayImage seillage(GrayImage im1, int s) {
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    for (int i = 0; i < result.getSurface(); i++) {
      int val = im1.read(i);
      if (val > s) {
        result.write(i, 0);
      } else
        result.write(i, 255);
    }
    return result;
  }
  
  public static GrayImage seillageInverse(GrayImage im1, int s) {
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    for (int i = 0; i < result.getSurface(); i++) {
      int val = im1.read(i);
      if (val < s) {
        result.write(i, 0);
      } else
        result.write(i, 255);
    }
    return result;
  }
  
  public static GrayImage inverse(GrayImage im1)
  {
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      int val = 255 - im1.read(i);
      result.write(i, val);
    }
    
    return result;
  }
  
  public static GrayImage plus(GrayImage im1, int h)
  {
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      int val = im1.read(i) + h;
      result.write(i, val);
    }
    
    return result;
  }
  
  public static boolean noirEtBlanc(GrayImage im1)
  {
    for (int i = 0; i < im1.getSurface(); i++) {
      if ((im1.read(i) != 0) && (im1.read(i) != 255)) { return false;
      }
    }
    return true;
  }
  
  public static GrayImage transformerNB(GrayImage im1)
  {
    GrayImage result = new GrayImage(im1.getHeight(), im1.getWidth());
    
    for (int i = 0; i < result.getSurface(); i++) {
      int val = 0;
      if (im1.read(i) > 127) val = 255;
      result.write(i, val);
    }
    
    return result;
  }
}
