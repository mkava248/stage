package lpe;



public class MorphologicalOperation
{
  private int[][] window;
  


  public MorphologicalOperation(boolean fourOrEight)
  {
    window = new int[3][3];
    
    if (fourOrEight) {
      window[0][0] = 0;
      window[0][1] = 1;
      window[0][2] = 0;
      window[1][0] = 1;
      window[1][1] = 1;
      window[1][2] = 1;
      window[2][0] = 0;
      window[2][1] = 1;
      window[2][2] = 0;
    } else {
      for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
          window[j][i] = 1;
    }
  }
  
  public GrayImage dilate(GrayImage gim, int size) {
    GrayImage out = dilate(gim);
    for (int j = 1; j < size; j++) {
      out = dilate(out);
    }
    return out;
  }
  
  public GrayImage erode(GrayImage gim, int size) {
    GrayImage out = erode(gim);
    for (int j = 1; j < size; j++) {
      out = erode(out);
    }
    return out;
  }
  
  public GrayImage open(GrayImage gim, int size) {
    GrayImage out = erode(gim, size);
    out = dilate(out, size);
    return out;
  }
  
  public GrayImage close(GrayImage gim, int size) {
    GrayImage out = dilate(gim, size);
    out = erode(out, size);
    return out;
  }
  
  public GrayImage OpenClose(GrayImage gim, int size) {
    GrayImage out = open(gim, size);
    out = close(gim, size);
    return out;
  }
  
  public GrayImage gradient(GrayImage gim, int size) {
    GrayImage dil = dilate(gim);
    GrayImage ero = erode(gim);
    for (int j = 1; j < size; j++) {
      dil = dilate(dil);
      ero = erode(ero);
    }
    return Operations.minus(dil, ero);
  }
  
  private GrayImage dilate(GrayImage gim)
  {
    GrayImage out = new GrayImage(gim.getHeight(), gim.getWidth());
    

    for (int i = 1; i < gim.getHeight() - 1; i++) {
      for (int j = 1; j < gim.getWidth() - 1; j++) {
        int maximum = 0;
        for (int k = 0; k < 3; k++) {
          for (int l = 0; l < 3; l++) {
            if ((window[k][l] != 0) && 
              (gim.read(i + k - 1, j + l - 1) > maximum))
              maximum = gim.read(i + k - 1, j + l - 1);
          }
        }
        out.write(i, j, maximum);
      }
    }
    return out;
  }
  
  private GrayImage erode(GrayImage gim)
  {
    GrayImage out = new GrayImage(gim);
    

    for (int i = 1; i < gim.getHeight() - 1; i++) {
      for (int j = 1; j < gim.getWidth() - 1; j++) {
        int minimum = 256;
        for (int k = 0; k < 3; k++) {
          for (int l = 0; l < 3; l++) {
            if (window[k][l] != 0)
            {
              if (gim.read(i + k - 1, j + l - 1) < minimum)
                minimum = gim.read(i + k - 1, j + l - 1); }
          }
        }
        out.write(i, j, minimum);
      }
    }
    return out;
  }
}
