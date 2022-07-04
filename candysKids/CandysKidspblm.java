
import java.util.*;
public class CandysKidspblm {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter Test Cases : ");
        int num_testCases = sc.nextInt();
        for(int i=0; i<num_testCases; i++){
            System.out.print("Enter Number of Bags: ");
            int bags = sc.nextInt();
            System.out.print("Enter Number of Kids: ");
            int kids = sc.nextInt();
            int sum = 0;
            for(int j=0; j< bags; j++){
                int eachCandys = sc.nextInt();
                sum += eachCandys;
            }

            System.out.print("Remaining Candys : " + sum % kids);
        }

    }
}
