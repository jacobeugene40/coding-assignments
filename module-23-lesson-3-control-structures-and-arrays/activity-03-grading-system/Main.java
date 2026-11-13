import java.util.*;

class Main {
  public static void main(String[] args) {
    int sum = 0;
    String result;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number of Subjects: ");
    int noOfSubjects = sc.nextInt();
    int marks[] = new int[noOfSubjects]; // initializing array
    System.out.println("Enter the marks of " + noOfSubjects + " Subjects.Press Enter to give marks for another subject");
    // entering marks
    for (int i = 0; i < noOfSubjects; i++) {
      marks[i] = sc.nextInt();
    }
    // calculating sum
    for (int j = 0; j < noOfSubjects; j++) {
      sum = sum + marks[j];
    }
    // percentage (average mark, out of 100); (double) keeps the decimals
    double percentage = sum / (double) noOfSubjects;
    System.out.println(percentage);

    // generating result (>= so that exactly 95 or 90 is not missed)
    if (percentage >= 95) {
      result = "You scored O grade. Great Work!";
    } else if (percentage >= 90) {
      result = "You scored A+.Well Done!";
    }
    // grading for the other marks, as the lesson suggests
    else if (percentage >= 80) {
      result = "You scored A. Good job!";
    } else if (percentage >= 70) {
      result = "You scored B. Keep going!";
    } else if (percentage >= 60) {
      result = "You scored C. You can do better!";
    } else if (percentage >= 50) {
      result = "You passed";
    } else {
      result = "You did not pass. Keep trying!";
    }
    System.out.println(result);
  }
}
