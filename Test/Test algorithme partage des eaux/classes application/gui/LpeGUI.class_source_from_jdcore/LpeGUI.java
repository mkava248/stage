package gui;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Window;
import java.awt.event.WindowEvent;
import javax.swing.AbstractButton;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.LineBorder;
import javax.swing.text.JTextComponent;

public class LpeGUI extends JFrame
{
  private JFileChooser fc;
  private GUIMetier metier;
  private final javax.swing.Icon openIcon = new javax.swing.ImageIcon("openfile.gif");
  private JButton jButton2;
  private JPanel jPanel16; private JPanel jPanel19; private JPanel jPanel13; private JPanel jPanel10; private JButton jButton3; private JLabel jLabel9;
  public static void main(String[] args) { LpeGUI frame = new LpeGUI();
    try
    {
      UIManager.setLookAndFeel(
        "com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
      SwingUtilities.updateComponentTreeUI(frame);
    }
    catch (Exception localException) {}
    
    frame.addWindowListener(new LpeGUI.1());
    



    frame.show(); }
  
  private JPanel jPanel12;
  private JComboBox jComboBox3;
  private JPanel jPanel7; private JPanel jPanel1; private JComboBox jComboBox2; private JTextField jTextField2;
  public LpeGUI() { super("LPE application");
    metier = new GUIMetier();
    initFileChooser();
    initComponents(); }
  
  private JPanel jPanel6;
  private JPanel jPanel14;
  private void initFileChooser() { fc = new JFileChooser();
    fc.setFileSelectionMode(0);
    LpeGUI.FcFileFilter filter = new LpeGUI.FcFileFilter(this, "jpg");
    fc.addChoosableFileFilter(filter);
    fc.setAcceptAllFileFilterUsed(false);
    try
    {
      UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
      SwingUtilities.updateComponentTreeUI(fc); } catch (Exception localException) {} }
  
  private JLabel jLabel6;
  private JComboBox jComboBox1;
  private JTextField jTextField1;
  private JLabel jLabel5;
  private JLabel jLabel4;
  private JLabel jLabel8;
  private JLabel jLabel12;
  private JPanel jPanel4;
  private JComboBox jComboBox4;
  private void initComponents() { jPanel1 = new JPanel();
    jPanel2 = new JPanel();
    jPanel3 = new JPanel();
    jPanel5 = new JPanel();
    jPanel10 = new JPanel();
    jPanel12 = new JPanel();
    jLabel3 = new JLabel();
    jPanel13 = new JPanel();
    jLabel7 = new JLabel();
    jComboBox1 = new JComboBox();
    jPanel11 = new JPanel();
    jPanel14 = new JPanel();
    jLabel4 = new JLabel();
    jPanel15 = new JPanel();
    jPanel22 = new JPanel();
    jLabel8 = new JLabel();
    jComboBox2 = new JComboBox();
    jPanel23 = new JPanel();
    jLabel9 = new JLabel();
    jComboBox3 = new JComboBox();
    jPanel24 = new JPanel();
    jLabel10 = new JLabel();
    jComboBox4 = new JComboBox();
    jPanel6 = new JPanel();
    jLabel1 = new JLabel();
    jPanel4 = new JPanel();
    jPanel7 = new JPanel();
    jPanel16 = new JPanel();
    jPanel18 = new JPanel();
    jLabel5 = new JLabel();
    jPanel20 = new JPanel();
    jLabel11 = new JLabel();
    jTextField1 = new JTextField();
    jButton3 = new JButton();
    jPanel17 = new JPanel();
    jPanel19 = new JPanel();
    jLabel6 = new JLabel();
    jPanel21 = new JPanel();
    jLabel12 = new JLabel();
    jComboBox5 = new JComboBox();
    jPanel8 = new JPanel();
    jLabel2 = new JLabel();
    jPanel9 = new JPanel();
    jButton1 = new JButton();
    jButton2 = new JButton();
    jPanel25 = new JPanel();
    jLabel13 = new JLabel();
    jTextField2 = new JTextField();
    jButton4 = new JButton();
    
    addWindowListener(new LpeGUI.2(this));
    




    jPanel1.setLayout(new BorderLayout());
    
    jPanel2.setLayout(new GridLayout(2, 0));
    
    jPanel3.setLayout(new BorderLayout());
    
    jPanel5.setLayout(new GridLayout(2, 0));
    
    jPanel10.setLayout(new GridLayout(1, 2));
    
    jPanel12.setLayout(new FlowLayout(0));
    
    jPanel12.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel3.setForeground(Color.blue);
    jLabel3.setText("Filtre moyenneur");
    jPanel12.add(jLabel3);
    
    jPanel10.add(jPanel12);
    
    jPanel13.setLayout(new FlowLayout(0));
    
    jPanel13.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel7.setText("Taille de la fenêtre : ");
    jPanel13.add(jLabel7);
    
    jComboBox1.addItem("");
    jComboBox1.addItem("1x1");
    jComboBox1.addItem("2x2");
    jComboBox1.addItem("3x3");
    jComboBox1.addItem("4x4");
    jComboBox1.addItem("5x5");
    jComboBox1.addItem("6x6");
    jComboBox1.addItem("7x7");
    jComboBox1.addItem("8x8");
    jComboBox1.addItem("9x9");
    jComboBox1.addItem("10x10");
    jComboBox1.addItem("11x11");
    jComboBox1.addItem("12x12");
    jComboBox1.addItem("13x13");
    jComboBox1.addItem("14x14");
    jComboBox1.addItem("15x15");
    jComboBox1.setEnabled(true);
    jComboBox1.setEditable(false);
    jComboBox1.addActionListener(new LpeGUI.3(this));
    














    jPanel13.add(jComboBox1);
    
    jPanel10.add(jPanel13);
    
    jPanel5.add(jPanel10);
    
    jPanel11.setLayout(new GridLayout(1, 2));
    
    jPanel14.setLayout(new FlowLayout(0));
    
    jPanel14.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel4.setForeground(Color.blue);
    jLabel4.setText("Filtre altérné séquentiel");
    jPanel14.add(jLabel4);
    
    jPanel11.add(jPanel14);
    
    jPanel15.setLayout(new GridLayout(3, 0));
    
    jPanel15.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jPanel22.setLayout(new FlowLayout(0));
    
    jLabel8.setText("Element 1 : ");
    jPanel22.add(jLabel8);
    
    jComboBox2.addItem("");
    
    for (int i = 0; i < 7; i++) {
      jComboBox2.addItem("" + i);
    }
    jComboBox2.setEnabled(true);
    jComboBox2.setEditable(false);
    jComboBox2.addActionListener(new LpeGUI.4(this));
    

























    jPanel22.add(jComboBox2);
    
    jPanel15.add(jPanel22);
    
    jPanel23.setLayout(new FlowLayout(0));
    
    jLabel9.setText("Element 2 : ");
    jPanel23.add(jLabel9);
    
    jComboBox3.addItem("");
    
    for (int i = 0; i < 7; i++) {
      jComboBox3.addItem("" + i);
    }
    jComboBox3.setEnabled(false);
    jComboBox3.setEditable(false);
    jComboBox3.addActionListener(new LpeGUI.5(this));
    

























    jPanel23.add(jComboBox3);
    
    jPanel15.add(jPanel23);
    
    jPanel24.setLayout(new FlowLayout(0));
    
    jLabel10.setText("Element 3 : ");
    jPanel24.add(jLabel10);
    
    jComboBox4.addItem("");
    
    for (int i = 0; i < 7; i++) {
      jComboBox4.addItem("" + i);
    }
    jComboBox4.setEnabled(false);
    jComboBox4.setEditable(false);
    jComboBox4.addActionListener(new LpeGUI.6(this));
    















    jPanel24.add(jComboBox4);
    
    jPanel15.add(jPanel24);
    
    jPanel11.add(jPanel15);
    
    jPanel5.add(jPanel11);
    
    jPanel3.add(jPanel5, "Center");
    
    jPanel6.setBackground(Color.orange);
    jPanel6.setBorder(
      new LineBorder(new Color(51, 51, 255)));
    jLabel1.setText("Pré-traitement");
    jPanel6.add(jLabel1);
    
    jPanel3.add(jPanel6, "North");
    
    jPanel2.add(jPanel3);
    
    jPanel4.setLayout(new BorderLayout());
    
    jPanel7.setLayout(new GridLayout(2, 0));
    
    jPanel16.setLayout(new GridLayout(1, 2));
    
    jPanel18.setLayout(new FlowLayout(0));
    
    jPanel18.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel5.setForeground(Color.blue);
    jLabel5.setText("Par marqueurs");
    jPanel18.add(jLabel5);
    
    jPanel16.add(jPanel18);
    
    jPanel20.setLayout(new FlowLayout(0));
    
    jPanel20.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel11.setText("Image des marqueurs : ");
    jPanel20.add(jLabel11);
    
    jTextField1.setText(
      "                                                     ");
    jTextField1.getDocument().addDocumentListener(new LpeGUI.7(this));
    



























    jPanel20.add(jTextField1);
    
    jButton3.setText("...");
    jButton3.setIcon(openIcon);
    jButton3.addActionListener(new LpeGUI.8(this));
    









    jPanel20.add(jButton3);
    
    jPanel16.add(jPanel20);
    
    jPanel7.add(jPanel16);
    
    jPanel17.setLayout(new GridLayout(1, 2));
    
    jPanel19.setLayout(new FlowLayout(0));
    
    jPanel19.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel6.setForeground(Color.blue);
    jLabel6.setText("Par le contraste");
    jPanel19.add(jLabel6);
    
    jPanel17.add(jPanel19);
    
    jPanel21.setLayout(new FlowLayout(0));
    
    jPanel21.setBorder(
      new LineBorder(new Color(0, 0, 0)));
    jLabel12.setText("Contraste seuil : ");
    jPanel21.add(jLabel12);
    
    jComboBox5.addItem("");
    
    for (int i = 1; i < 256; i++) {
      jComboBox5.addItem("" + i);
    }
    jComboBox5.setEnabled(true);
    jComboBox5.setEditable(false);
    jComboBox5.addActionListener(new LpeGUI.9(this));
    















    jPanel21.add(jComboBox5);
    
    jPanel17.add(jPanel21);
    
    jPanel7.add(jPanel17);
    
    jPanel4.add(jPanel7, "Center");
    
    jPanel8.setBackground(Color.orange);
    jPanel8.setBorder(
      new LineBorder(new Color(51, 51, 255)));
    jLabel2.setText("Contraites");
    jPanel8.add(jLabel2);
    
    jPanel4.add(jPanel8, "North");
    
    jPanel2.add(jPanel4);
    
    jPanel1.add(jPanel2, "Center");
    
    jPanel9.setLayout(new FlowLayout(2));
    
    jButton1.setBackground(Color.orange);
    jButton1.setForeground(Color.blue);
    jButton1.setText("Calculer la LPE");
    jButton1.addActionListener(new LpeGUI.10(this));
    




    jPanel9.add(jButton1);
    
    jButton2.setBackground(Color.orange);
    jButton2.setForeground(new Color(0, 0, 0));
    jButton2.setText("Quiter");
    jButton2.addActionListener(new LpeGUI.11(this));
    



    jPanel9.add(jButton2);
    
    jPanel1.add(jPanel9, "South");
    
    getContentPane().add(jPanel1, "Center");
    
    jLabel13.setForeground(Color.blue);
    jLabel13.setText("Image initiale");
    jPanel25.add(jLabel13);
    
    jTextField2.setText(
      "                                                     ");
    jPanel25.add(jTextField2);
    
    jButton4.setText("...");
    jButton4.setIcon(openIcon);
    jButton4.addActionListener(new LpeGUI.12(this));
    








    jPanel25.add(jButton4);
    
    getContentPane().add(jPanel25, "North");
    
    pack(); }
  
  private JLabel jLabel1;
  private JLabel jLabel3;
  private void lpe() { String init = jTextField2.getText().trim();
    
    if (init.length() == 0) { return;
    }
    metier.loadImage(init);
    
    String mark = jTextField1.getText().trim();
    
    if (mark.length() == 0) {
      metier.marqueur = false;
    } else {
      metier.marqueur = true;
      metier.loadMarqueur(mark);
    }
    
    metier.go(); }
  
  private JPanel jPanel25;
  private JLabel jLabel13;
  private JPanel jPanel3;
  private void quit() { System.exit(0); }
  
  private JLabel jLabel2;
  private JButton jButton1;
  
  private void exitForm(WindowEvent evt) {
    quit(); }
  
  private JPanel jPanel24;
  private JPanel jPanel2;
  private JPanel jPanel5;
  private JPanel jPanel11;
  private JComboBox jComboBox5;
  private JPanel jPanel8;
  private JPanel jPanel22;
  private JLabel jLabel11;
  private JLabel jLabel7;
  private JPanel jPanel18;
  private JPanel jPanel17;
  private JPanel jPanel21;
  private JButton jButton4;
  private JPanel jPanel20;
  private JPanel jPanel15;
  private JPanel jPanel9;
  private JPanel jPanel23;
  private JLabel jLabel10;
}
