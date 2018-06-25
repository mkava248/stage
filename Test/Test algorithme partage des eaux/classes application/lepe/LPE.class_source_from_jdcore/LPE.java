package lpe;

import java.util.Vector;












public class LPE
{
  public static final int INIT = -1;
  public static final int MASK = -2;
  public static final int WSHED = 0;
  private final int MARK = -1;
  


  private GrayImage in;
  


  public int numberLabel;
  


  public int[] histogramme;
  


  public GrayImage sortedImage;
  


  private int[] sortedPixels;
  


  public LPE(GrayImage gi)
  {
    in = gi;
    histo();
    sortImage();
  }
  



  private void histo()
  {
    int[] hist = new int['Ā'];
    
    for (int k = 0; k < 256; k++) {
      hist[k] = 0;
    }
    for (int i = 0; i < in.getHeight(); i++) {
      for (int j = 0; j < in.getWidth(); j++)
        hist[in.read(i, j)] += 1;
    }
    histogramme = hist;
  }
  



  private void sortImage()
  {
    GrayImage sgi = new GrayImage(in.getHeight(), in.getWidth());
    int px = 0;
    
    for (int k = 0; k < 256; k++) {
      for (int j = 0; j < histogramme[k]; j++) {
        sgi.write(px, k);
        px++;
      }
    }
    sortedImage = sgi;
    

    sortedPixels = new int[in.getSurface()];
    



    int[] index = new int[in.getSurface()];
    int s = 0;
    for (int i = 0; i < 256; i++) {
      index[i] = s;
      s += histogramme[i];
    }
    




    for (int pix = 0; pix < in.getSurface(); pix++) {
      int val = in.read(pix);
      int position = index[val];
      
      sortedPixels[position] = pix;
      index[val] += 1;
    }
  }
  



















  private boolean isNeighbour(int height, int width, int row, int column, int varRow, int varCol, boolean fourOrEight)
  {
    if ((row + varRow >= 0) && 
      (row + varRow < height) && 
      (column + varCol >= 0) && 
      (column + varCol < width)) {
      if (fourOrEight) {
        return 
          ((varRow == 0) && (varCol != 0)) || (
          (varRow != 0) && (varCol == 0));
      }
      return (varRow != 0) || (varCol != 0);
    }
    
    return false;
  }
  








  public GrayImage runLPE(boolean fourOrEight, boolean separation)
  {
    GrayImage lab = new GrayImage(in.getHeight(), in.getWidth());
    
    GrayImage dist = new GrayImage(in.getHeight(), in.getWidth());
    

    int curlab = 0;
    
    Fifo pile = new Fifo();
    

    for (int p = 0; p < in.getSurface(); p++) {
      lab.write(p, -1);
      dist.write(p, 0);
    }
    


    int curHistPos = 0;
    
    for (int h = 0; h < 256; h++) {
      for (int index = curHistPos; index < curHistPos + histogramme[h]; index++) {
        int curPix = sortedPixels[index];
        
        lab.write(curPix, -2);
        
        int row = lab.getRowFromAbsolutePosition(curPix);
        int column = lab.getColumnFromAbsolutePosition(curPix);
        
        boolean done = false;
        for (int varRow = -1; (varRow <= 1) && (!done); varRow++) {
          for (int varCol = -1; 
              (varCol <= 1) && (!done); 
              varCol++)
          {

            if (isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol, fourOrEight)) {
              if ((lab.read(varRow + row, varCol + column) > 0) || 
                (lab.read(varRow + row, varCol + column) == 0))
              {
                dist.write(curPix, 1);
                pile.push(curPix);
                done = true;
              }
            }
          }
        }
      }
      int curDist = 1;
      
      pile.push(-1);
      
      for (;;)
      {
        int curPix = pile.pop();
        if (curPix == -1) {
          if (pile.isEmpty()) {
            break;
          }
          pile.push(-1);
          curDist++;
          curPix = pile.pop();
        }
        

        int row = lab.getRowFromAbsolutePosition(curPix);
        int column = lab.getColumnFromAbsolutePosition(curPix);
        
        for (int varRow = -1; varRow <= 1; varRow++) {
          for (int varCol = -1; varCol <= 1; varCol++) {
            if (isNeighbour(lab.getHeight(), lab.getWidth(), row, column, varRow, varCol, fourOrEight)) {
              int neighbourPos = 
                lab.getAbsolutePosition(
                row + varRow, 
                column + varCol);
              if ((dist.read(neighbourPos) < curDist) && (
                (lab.read(neighbourPos) > 0) || 
                (lab.read(neighbourPos) == 0))) {
                if (lab.read(neighbourPos) > 0) {
                  if ((lab.read(curPix) == -2) || 
                    (lab.read(curPix) == 0)) {
                    lab.write(
                      curPix, 
                      lab.read(neighbourPos));
                  }
                  else if (lab.read(curPix) != 
                    lab.read(neighbourPos)) {
                    lab.write(curPix, 0);
                  }
                }
                else if (lab.read(curPix) == -2) {
                  lab.write(curPix, 0);
                }
              }
              else if ((lab.read(neighbourPos) == -2) && 
                (dist.read(neighbourPos) == 0)) {
                dist.write(neighbourPos, curDist + 1);
                pile.push(neighbourPos);
              }
            }
          }
        }
      }
      
      for (int index = curHistPos; 
          index < curHistPos + histogramme[h]; 
          index++) {
        int curPix = sortedPixels[index];
        dist.write(curPix, 0);
        if (lab.read(curPix) == -2) {
          curlab++;
          pile.push(curPix);
          lab.write(curPix, curlab);
          int varRow; for (; !pile.isEmpty(); 
              




              varRow <= 1)
          {
            curPix = pile.pop();
            
            int row = lab.getRowFromAbsolutePosition(curPix);
            int column = lab.getColumnFromAbsolutePosition(curPix);
            
            varRow = -1; continue;
            for (int varCol = -1; varCol <= 1; varCol++) {
              if (isNeighbour(lab.getHeight(), 
                lab.getWidth(), 
                row, 
                column, 
                varRow, 
                varCol, 
                fourOrEight)) {
                int neighbourPos = 
                  lab.getAbsolutePosition(
                  row + varRow, 
                  column + varCol);
                if (lab.read(neighbourPos) == -2) {
                  pile.push(neighbourPos);
                  lab.write(neighbourPos, curlab);
                }
              }
            }
            varRow++;
          }
        }
      }
      


















      curHistPos += histogramme[h];
    }
    
    numberLabel = curlab;
    

    if (separation) {
      for (int curPix = 0; curPix < lab.getSurface(); curPix++) {
        if (lab.read(curPix) > 0)
        {
          int row = lab.getRowFromAbsolutePosition(curPix);
          int column = lab.getColumnFromAbsolutePosition(curPix);
          
          boolean done = false;
          for (int varRow = -1; 
              (varRow <= 1) && (!done); 
              varRow++) {
            for (int varCol = -1; 
                (varCol <= 1) && (!done); 
                varCol++) {
              if (isNeighbour(lab.getHeight(), 
                lab.getWidth(), 
                row, 
                column, 
                varRow, 
                varCol, 
                fourOrEight)) {
                int neighbourPos = 
                  lab.getAbsolutePosition(
                  row + varRow, 
                  column + varCol);
                if ((lab.read(curPix) > lab.read(neighbourPos)) && 
                  (lab.read(neighbourPos) > 0)) {
                  lab.write(curPix, 0);
                  done = true;
                }
              }
            }
          }
        }
      }
    }
    return lab;
  }
}
