import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

public class NameNode {
    // DataNode heartbeat threshold in milliseconds
    private static final long HEARTBEAT_THRESHOLD = 5000;
    // Map to keep track of DataNode IDs and their last heartbeat time
    private static ConcurrentHashMap<String, Long> activeDataNodes = new ConcurrentHashMap<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            System.out.println("NameNode is running...");

            // Thread to monitor heartbeat of DataNodes
            new Thread(() -> {
                while (true) {
                    long currentTime = System.currentTimeMillis();
                    for (String nodeId : activeDataNodes.keySet()) {
                        long lastHeartbeat = activeDataNodes.get(nodeId);
                        if (currentTime - lastHeartbeat > HEARTBEAT_THRESHOLD) {
                            System.out.println("DataNode " + nodeId + " is DOWN.");
                            activeDataNodes.remove(nodeId);
                        }
                    }
                    try {
                        Thread.sleep(2000); // Monitor every 2 seconds
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            }).start();

            // Main loop to accept heartbeats from DataNodes
            while (true) {
                Socket socket = serverSocket.accept();
                new Thread(new DataNodeHandler(socket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Class to handle heartbeats from DataNodes
    static class DataNodeHandler implements Runnable {
        private Socket socket;

        public DataNodeHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
                String nodeId;
                while ((nodeId = in.readLine()) != null) {
                    // Update the last heartbeat time for the DataNode
                    activeDataNodes.put(nodeId, System.currentTimeMillis());
                    System.out.println("Received heartbeat from DataNode " + nodeId);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

