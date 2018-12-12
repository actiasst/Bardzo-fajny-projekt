import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class convertPNGtoJPG {

    public static void main(String[] args) {
        File folder = new File(args[0]);
        File[] listOfFiles = folder.listFiles();

        BufferedImage bufferedImage;
        try {
            for(int i = 0; i < listOfFiles.length; i++) {
                bufferedImage = ImageIO.read(new File(args[0]+"\\"+listOfFiles[i].getName()));
                String name = "";
                for(int j = 0; j < listOfFiles[i].getName().length() - 4; j++){
                     name += listOfFiles[i].getName().charAt(j);
                }

                BufferedImage newBufferedImage = new BufferedImage(bufferedImage.getWidth(),
                        bufferedImage.getHeight(), BufferedImage.TYPE_INT_RGB);
                newBufferedImage.createGraphics().drawImage(bufferedImage, 0, 0, Color.WHITE, null);
                ImageIO.write(newBufferedImage, "jpg", new File(args[0]+"\\" + name + ".jpg"));
                File file = new File(args[0]+"\\"+listOfFiles[i].getName());
                file.delete();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
