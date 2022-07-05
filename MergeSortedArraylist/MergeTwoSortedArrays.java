
import java.util.*;
public class MergeTwoSortedArrays {
    public static void main (String[] args) {
        //Array 1
        int[] arr1 = {11, 34, 66, 75};
        int n1 = arr1.length;

        //Array 2
        int[] arr2 = {1, 5, 19, 50, 89, 100};
        int n2 = arr2.length;

        ArrayList<Integer> finalList = new ArrayList<Integer>();

        int i = 0, j = 0;
        while (i < n1 && j < n2) {
            if (arr1[i] < arr2[j]) {
                finalList.add(arr1[i]);
                i+=1;
            } else{
                finalList.add(arr2[j]);
                j+=1;
            }
        }

        System.out.print("\nArray after merging: " + finalList);
    }

}
