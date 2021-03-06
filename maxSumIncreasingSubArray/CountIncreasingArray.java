public class CountIncreasingArray {
        static int maxSum(int arr[], int n)
        {
            // max_sum be 0
            int max_sum = arr[0];

            // current sum be arr[0]
            int current_sum = arr[0];

            for (int i = 1; i < n; i++)
            {
                if (arr[i - 1] < arr[i])
                {
                    current_sum = current_sum + arr[i];
                    max_sum = Math.max(max_sum, current_sum);
                }
                else
                {
                    max_sum = Math.max(max_sum, current_sum);
                    current_sum = arr[i];
                }
            }

            return Math.max(max_sum, current_sum);
        }

        // Driver code
        public static void main(String[] args)
        {
            int arr[] = { 1, 2, 2, 4 };
            System.out.println("Maximum sum of increasing sub array is: " + maxSum(arr, arr.length));
        }

}
