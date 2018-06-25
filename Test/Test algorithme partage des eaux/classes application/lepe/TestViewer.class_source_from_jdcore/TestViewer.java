package lpe;

import java.awt.Component;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.MediaTracker;
import java.awt.Window;
import java.io.PrintStream;


public class TestViewer
  extends Frame
{
  Image image;
  
  public TestViewer(Image im)
  {
    image = im;
    MediaTracker mediaTracker = new MediaTracker(this);
    mediaTracker.addImage(image, 0);
    try
    {
      mediaTracker.waitForID(0);
    }
    catch (InterruptedException ie)
    {
      System.err.println(ie);
      System.exit(1);
    }
    addWindowListener(new TestViewer.1(this));
    



    setSize(image.getWidth(null), image.getHeight(null));
    setTitle("image view");
    show();
  }
  
  public TestViewer(Image im, String s) {
    this(im);
    setTitle(s);
  }
  
  private void close() {
    hide();
  }
  
  public void paint(Graphics graphics) {
    graphics.drawImage(image, 0, 0, null);
  }
}
