package lpe;

import com.sun.image.codec.jpeg.JPEGCodec;
import com.sun.image.codec.jpeg.JPEGEncodeParam;
import com.sun.image.codec.jpeg.JPEGImageEncoder;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Random;



public class FactoryLPE
{
  private Image originalImage;
  private LPE lpe;
  
  public FactoryLPE(Image image)
  {
    originalImage = image;
    doLPE(image);
  }
  
  private void doLPE(Image im) {
    GrayImage gi = convertToGray(im).getGrayImage();
    lpe = new LPE(gi);
  }
  
  public static GrayBuffredImage convertToGray(Image im) {
    GrayBuffredImage gi = new GrayBuffredImage(im);
    gi.updateFromGrayImage(gi.getGrayImage());
    return gi;
  }
  
  public static GrayImage getGrayImage(Image im) {
    return convertToGray(im).getGrayImage();
  }
  
  public static Image readImageJPEG(String fileName) {
    return Toolkit.getDefaultToolkit().getImage(fileName);
  }
  
  public static void viewImage(Image im) {
    new TestViewer(im);
  }
  
  public static void viewImage(Image im, String s) {
    new TestViewer(im, s);
  }
  
  public static void writeImageJPEG(BufferedImage bi, String fileOut) {
    try {
      BufferedOutputStream out = 
        new BufferedOutputStream(new FileOutputStream(fileOut));
      JPEGImageEncoder encoder = JPEGCodec.createJPEGEncoder(out);
      JPEGEncodeParam param = encoder.getDefaultJPEGEncodeParam(bi);
      param.setQuality(1.0F, false);
      encoder.setJPEGEncodeParam(param);
      encoder.encode(bi);
    } catch (Exception e) {
      System.out.println(e);
    }
    System.out.println("Done.");
  }
  
  public static BufferedImage bufferedImageFromImage(Image image) {
    BufferedImage bi = 
      new BufferedImage(
      image.getWidth(null), 
      image.getHeight(null), 
      1);
    Graphics2D big = bi.createGraphics();
    big.drawImage(image, 0, 0, null);
    return bi;
  }
  









  public BufferedImage getGrayImage(boolean fourOrEight, boolean separation)
  {
    GrayImage labels = lpe.runLPE(fourOrEight, separation);
    
    for (int pix = 0; pix < labels.getSurface(); pix++) {
      int valLab = labels.read(pix);
      int newValLab = (valLab - 1) % 255 + 1;
      labels.write(pix, newValLab);
    }
    
    return new GrayBuffredImage(labels);
  }
  







  public BufferedImage getSeparationImage(boolean fourOrEight, boolean separation)
  {
    GrayImage labels = lpe.runLPE(fourOrEight, separation);
    
    for (int pix = 0; pix < labels.getSurface(); pix++) {
      int valLab = labels.read(pix);
      int newValLab = 255;
      if (valLab == 0)
        newValLab = 0;
      labels.write(pix, newValLab);
    }
    
    return new GrayBuffredImage(labels);
  }
  







  public BufferedImage getSeparationOnImage(boolean fourOrEight, boolean separation)
  {
    GrayImage labels = lpe.runLPE(fourOrEight, separation);
    
    BufferedImage bi = bufferedImageFromImage(originalImage);
    
    for (int pix = 0; pix < labels.getSurface(); pix++) {
      int valLab = labels.read(pix);
      if (valLab == 0) {
        int x = labels.getColumnFromAbsolutePosition(pix);
        int y = labels.getRowFromAbsolutePosition(pix);
        bi.setRGB(x, y, 0);
      }
    }
    return bi;
  }
  







  public BufferedImage getSeparationOnImage(boolean fourOrEight, boolean separation, Image image)
  {
    GrayImage labels = lpe.runLPE(fourOrEight, separation);
    
    BufferedImage bi = bufferedImageFromImage(image);
    
    for (int pix = 0; pix < labels.getSurface(); pix++) {
      int valLab = labels.read(pix);
      if (valLab == 0) {
        int x = labels.getColumnFromAbsolutePosition(pix);
        int y = labels.getRowFromAbsolutePosition(pix);
        bi.setRGB(x, y, 0);
      }
    }
    return bi;
  }
  









  public BufferedImage getColorsImage(boolean fourOrEight, boolean separation)
  {
    GrayImage labels = lpe.runLPE(fourOrEight, true);
    
    BufferedImage bi = bufferedImageFromImage(originalImage);
    
    int nb = lpe.numberLabel + 1;
    
    int[] correspondanceR = new int[nb];
    int[] correspondanceG = new int[nb];
    int[] correspondanceB = new int[nb];
    
    correspondanceR[0] = 0;
    correspondanceG[0] = 0;
    correspondanceB[0] = 0;
    
    Random rand = new Random();
    for (int i = 1; i < nb; i++) {
      correspondanceR[i] = (rand.nextInt(255) + 1);
      correspondanceG[i] = (rand.nextInt(255) + 1);
      correspondanceB[i] = (rand.nextInt(255) + 1);
    }
    
    for (int pix = 0; pix < labels.getSurface(); pix++) {
      int valLab = labels.read(pix);
      int x = labels.getColumnFromAbsolutePosition(pix);
      int y = labels.getRowFromAbsolutePosition(pix);
      Color cl = new Color(correspondanceR[valLab], correspondanceG[valLab], correspondanceB[valLab]);
      bi.setRGB(x, y, cl.getRGB());
    }
    return bi;
  }
}
