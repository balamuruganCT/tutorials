package hackerEarth;

import java.text.ParseException;
public class arrayRotationCertainTimes {
    public static void main(String[] args) throws ParseException {
        String s = "41023";

        int mid = s.length() / 2;

        String leftString = "";
        String rightString = "";
        for(int i=0; i<=mid-1; i++){
            leftString += s.charAt(i);
        }
        for(int i=mid+1; i<s.length(); i++){
            rightString += s.charAt(i);
        }

        int leftSum = 0;
        int rightSum = 0;
        for(int i=0; i<leftString.length(); i++){
            leftSum += (int)leftString.charAt(i);
        }

        for(int i=0; i<rightString.length(); i++){
            rightSum += (int)rightString.charAt(i);
        }

        if(leftSum == rightSum){
            System.out.println("True");
        }else {
            System.out.println("False");
        }

    }
}
