import java.util.*;
public class P32LinearSearch {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size");
        int n=sc.nextInt();
        System.out.println("Enter the eles");
        int a[]=new int[n];  
        for(int j=0;j<a.length;j++){
            a[j]=sc.nextInt();
        }

        System.out.println("Enter the ele to be searched");
        int c=sc.nextInt();
        for(int i=0;i<a.length;i++){
            if(a[i]==c)
            System.out.println(c+" found at "+i + "index");
        }
    }
}
