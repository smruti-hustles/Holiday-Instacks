import java.util.*;
public class P33BinarySearch{
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];

        //binary search works with sorted array
        System.out.println("Enter the elements in ascending or descending order:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        
        System.out.print("Enter the element to search: ");
        int key = scanner.nextInt();

        int l=0;
        int h=n-1;
        int mid;

        while(l<=h){
            mid=l+(h-l)/2;  // to reduce time complecity

            if(arr[mid]==key){
                System.out.println("Element found at index: " + mid);
                return;
            }
            else if(arr[mid]<key){
                l=mid+1;
            }
            else if(arr[mid]>key){
                h=mid-1;
            }
        }
        System.out.println("Element not found.");
       
    }
}