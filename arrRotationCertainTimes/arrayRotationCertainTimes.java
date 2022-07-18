package hackerEarth;

public class arrayRotationCertainTimes {
    public static void arrayRotation(int[] arr, int k, int n){
        int index = n - (k % n);

        for(int i=index; i<n; i++){
            System.out.print(arr[i] + " ");
        }
        for(int i=0; i<index; i++){
            System.out.print(arr[i]+ " ");
        }

    }
    public static void main(String[] args){
        int[] array = new int[]{ 1,2,3,4,5};
        int k = 2;
        arrayRotation(array, k, array.length);
    }
}
