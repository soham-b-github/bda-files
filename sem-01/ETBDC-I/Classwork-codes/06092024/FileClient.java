import java.io.FileInputStream;
import java.io.OutputStream;
import java.net.Socket;

public class FileClient {
    public static void main(String[] args) {
        String filePath = "test.txt"; // Replace with the path to the existing file you want to send

        try (Socket socket = new Socket("localhost", 8080)) {
            System.out.println("Connected to server.");

            // Send the file to server
            FileInputStream fileInputStream = new FileInputStream(filePath);
            OutputStream outputStream = socket.getOutputStream();

            byte[] buffer = new byte[4096];
            int bytesRead;
            System.out.println("Sending file...");
            while ((bytesRead = fileInputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }

            fileInputStream.close();
            socket.close();
            System.out.println("File sent successfully.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
