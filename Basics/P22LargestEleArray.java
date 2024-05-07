import java.util.*;
public class P22LargestEleArray{
    public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int a[]=new int[n];
for(int i=0;i<a.length;i++){
    a[i]=sc.nextInt();
}
Arrays.sort(a);
System.out.println("Max ele is : "+a[a.length-1]);
System.out.println("Min ele is : "+a[0]);
System.out.println("2nd largest ele "+a[a.length-2]);
System.out.println("2nd smallest ele "+a[1]);
}
}
