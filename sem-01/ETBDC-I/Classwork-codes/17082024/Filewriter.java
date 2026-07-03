import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Filewriter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String fileName = "student_details.csv";

        try (FileWriter writer = new FileWriter(fileName)) {
            // Write the header row
            writer.append("Name,Age,Grade\n");

            while (true) {
                System.out.println("Enter student details:");

                System.out.print("Name: ");
                String name = scanner.nextLine();

                System.out.print("Age: ");
                String age = scanner.nextLine();

                System.out.print("Grade: ");
                String grade = scanner.nextLine();

                // Write the student details to the CSV file
                writer.append(name)
                      .append(',')
                      .append(age)
                      .append(',')
                      .append(grade)
                      .append('\n');

                System.out.println("Student details saved.");

                System.out.print("Do you want to enter details for another student? (yes/no): ");
                String choice = scanner.nextLine();

                if (choice.equalsIgnoreCase("no")) {
                    break;
                }
            }

            System.out.println("All student details have been saved to " + fileName);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        scanner.close();
    }
}
