
import java.util.Arrays;

/**
 * @author Balamurugan V
 * @project code.tamil
 * @created 25/07/2022
 **/
public class XOR {
    public static void main(String[] args){
        int[] arr = {1, 2, 3, 4, 5, 6};
        Arrays.sort(arr);
        if(arr.length < 2){
            System.out.println("array size must be greater the or equal to 2.");
        }
        int minimum = arr[0] ^ arr[1];
        for(int i=1; i<arr.length - 1 ;i++){
            int current = arr[i] ^ arr[i+1];
            if(current < minimum){
                minimum = current;
            }
        }
        System.out.println("minimum xor value : " + minimum);
    }
}
