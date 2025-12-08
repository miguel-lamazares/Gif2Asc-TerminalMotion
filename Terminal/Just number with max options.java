public class JustNumber {
    public static int readInt(java.util.Scanner scanner, int maxvalue) {
        int choice;
        while (true) {
            if (!scanner.hasNextInt()) {
                scanner.nextLine(); 
                System.out.print("\033[1A");
                System.out.print("\033[2K");

                continue;
            }
            choice = scanner.nextInt();
            scanner.nextLine();

            if(choice >= maxvalue){
                System.out.print("\033[1A");
                System.out.print("\033[2K");
                continue;
            }

            return choice;
        }
    }
