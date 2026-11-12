package CodeForces; 

import java.util.Scanner; 

public class J1807A {

    public static String PlusOrMinus(int a, int b, int c){
        if(a + b == c) {
            return "+"; 
        }
        else {
            return "-"; 
        }    
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 

        int t; 
        t = sc.nextInt(); 
        while(t > 0) {
            int a = sc.nextInt(); 
            int b = sc.nextInt(); 
            int c = sc.nextInt(); 
            System.out.println(PlusOrMinus(a, b, c));
            t--; 
        }
    }
}