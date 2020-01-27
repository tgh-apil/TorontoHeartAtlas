import java.util.Scanner;
public class test{
    public static void main(String arg[]){

        System.out.println("Enter a name");
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();

        int length = name.length();
        System.out.println(length);

        if (name.length() <= 3){
            System.out.println("Short name");
        } else if (name.length() <= 6){
            System.out.println("Regular name");
        } else {
            System.out.println("fuckin massive name bruv");
        }
    }
}