import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.Arrays;

public class namedScores {   

  public static int score(String name) {
    name = name.substring(1, name.length() - 1);
    int total = 0;
    for (int i = 0; i < name.length(); ++i) {
      int x = name.charAt(i) - 'A' + 1;
      total = total + x;
    }
    return total;
  }

  public static void main(String args[]) {
    
    //reading file line by line in Java using BufferedReader       
    FileInputStream fis = null;
    BufferedReader reader = null;
  
    long total = 0;
    try {
        fis = new FileInputStream("names.txt");
        reader = new BufferedReader(new InputStreamReader(fis));      
        String line = reader.readLine();
        String[] names = line.split(",");
        //System.out.println(names.length);
        Arrays.sort(names);
        for (int i = 0 ; i< names.length; i++) {
          int nameScore = score(names[i]);
          total = total + nameScore*(i+1);
        }
    } catch (FileNotFoundException ex) {
        Logger.getLogger(namedScores.class.getName()).log(Level.SEVERE, null, ex);
    } catch (IOException ex) {
        Logger.getLogger(namedScores.class.getName()).log(Level.SEVERE, null, ex);
    } finally {
        try {
            reader.close();
            fis.close();
        } catch (IOException ex) {
            Logger.getLogger(namedScores.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    System.out.println("Total is: " + total);
  }
}