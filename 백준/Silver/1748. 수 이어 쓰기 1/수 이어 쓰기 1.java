import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int sum = 0;
        
        for (int i = 1; i <= N; i*=10) {
            sum += (N-i)+1;
        }

        System.out.println(sum);
    }
}