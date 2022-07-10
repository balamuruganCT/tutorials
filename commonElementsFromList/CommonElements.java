
import java.util.*;

public class CommonElements {
    public static void main(String[] args){
        int[] arr1 = {1, 3, 4, 6, 7, 9};
        int[] arr2 = {1, 2, 4, 5, 9, 10};
        int p1 = 0;
        int p2 = 0;
        ArrayList<Integer> newList = new ArrayList<>();
        while (p1 < arr1.length && p2 < arr2.length){
            if (arr1[p1] == arr2[p2]){
                newList.add(arr1[p1]);
                p1+=1;
                p2+=1;
            }else if (arr1[p1] > arr2[p2]){
                p2 +=1;
            }else{
                p1+=1;
            }
        }
        System.out.println("Final List: " + newList);
    }
}
