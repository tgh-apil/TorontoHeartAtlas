import java.util.Scanner;
public class test{
    public static void main(String arg[]){
        System.out.println("hello");
        System.out.println("fineman is a god");

        System.out.println("Enter a name");
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();

        if (name.length() == 3){
            System.out.println("Short name");
        } else {
            System.out.println("Regular name");
        }
    }
}