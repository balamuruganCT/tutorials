package io.jenkins.plugins.jenkinsHelloWorld;

public class StrPattern {
    public static void main(String[] args){
        int n = 6;
        for(int i=0; i<n; i++){
            for(int j=n-i; j>1; j--)
            {
                System.out.println(" ");
            }
            for(int j=0; j<=i; j++)
            {
                System.out.println("* ");
            }
            System.out.println();
        }
    }
}
