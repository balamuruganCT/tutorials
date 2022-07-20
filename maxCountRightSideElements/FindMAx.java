package hackerEarth;

import java.util.ArrayList;

public class FindMAx {
    public static void main(String[] args){
        ArrayList<Integer> finalArrayList = new ArrayList<>();
        int[] arr = {1, 2, 3, 5, 1, 3, 4};
        for (int i=0; i<arr.length; i++){
            int count = 0;
            for(int j=i; j<arr.length;j++){
                if(arr[i] < arr[j]){
                    count +=1;
                }
            }
            finalArrayList.add(count);
        }
        System.out.println("final Array list :" + finalArrayList);
    }
}
