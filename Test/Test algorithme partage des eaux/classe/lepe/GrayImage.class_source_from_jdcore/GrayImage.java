package lpe;



public class GrayImage
{
  private int[][] pixels;
  

  private int width;
  

  private int height;
  

  private int surface;
  

  public GrayImage(int h, int w)
  {
    height = h;
    width = w;
    surface = (h * w);
    pixels = new int[height][width];
  }
  






  public GrayImage(int h, int w, int[][] p)
  {
    this(h, w);
    pixels = p;
  }
  



  public GrayImage(GrayImage gim)
  {
    this(gim.getHeight(), gim.getWidth());
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        pixels[i][j] = gim.read(i, j);
      }
    }
  }
  



  public int read(int i, int j)
  {
    return pixels[i][j];
  }
  





  public void write(int i, int j, int value)
  {
    pixels[i][j] = value;
  }
  





  public int read(int p)
  {
    int i = p / width;
    int j = p % width;
    
    return pixels[i][j];
  }
  




  public void write(int p, int value)
  {
    int i = p / width;
    int j = p % width;
    
    pixels[i][j] = value;
  }
  



  public int getHeight()
  {
    return height;
  }
  



  public int getWidth()
  {
    return width;
  }
  



  public int getSurface()
  {
    return surface;
  }
  




  public int getRowFromAbsolutePosition(int pos)
  {
    return pos / width;
  }
  




  public int getColumnFromAbsolutePosition(int pos)
  {
    return pos % width;
  }
  





  public int getAbsolutePosition(int row, int column)
  {
    return row * width + column;
  }
}
