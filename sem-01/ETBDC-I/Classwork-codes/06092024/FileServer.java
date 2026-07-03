import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class FileServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            System.out.println("Server is listening on port 8080...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client connected.");

                // Receive the file from client
                InputStream inputStream = socket.getInputStream();
                FileOutputStream fileOutputStream = new FileOutputStream("received_file");

                byte[] buffer = new byte[4096];
                int bytesRead;
                System.out.println("Receiving file...");
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    fileOutputStream.write(buffer, 0, bytesRead);
                }

                fileOutputStream.close();
                socket.close();
                System.out.println("File received and saved as 'received_file'.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

