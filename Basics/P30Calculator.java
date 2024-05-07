import java.util.*;
public class P30Calculator{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.next().charAt(0);
        switch(c){
        case '+':System.out.println(a+b);break;
        case '-':System.out.println(a-b);break;
        case '*':System.out.println(a*b);break;
        case '/':System.out.println(a/b);break;
        case '%':System.out.println(a%b);break;  
        default:System.out.println("choose some other character...invalid input");      
        }
    }
}