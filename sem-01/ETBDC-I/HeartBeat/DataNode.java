import java.io.*;
import java.net.*;
import java.util.*;

public class DataNode 
{
    private static final long HEARTBEAT_INTERVAL = 3000; // Heartbeat interval in milliseconds
    private static final String NAMENODE_HOST = "localhost";
    private static final int NAMENODE_PORT = 8080;
    private static String nodeId;

    public static void main(String[] args) 
    {
        // Generate a unique DataNode ID
        nodeId = UUID.randomUUID().toString();
        
        try (Socket socket = new Socket(NAMENODE_HOST, NAMENODE_PORT);  PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) 
        {    
            System.out.println("DataNode " + nodeId + " is running and sending heartbeats...");
            
            // Periodically send heartbeat messages to the NameNode
            while (true) 
            {
                out.println(nodeId); // Send DataNode ID as heartbeat
                System.out.println("Sent heartbeat from DataNode " + nodeId);
                Thread.sleep(HEARTBEAT_INTERVAL);
            }
        } 
        catch (IOException | InterruptedException e) 
        {
            e.printStackTrace();
        }
    }
}

