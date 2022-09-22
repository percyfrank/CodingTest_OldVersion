import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(sc.hasNextInt()) {
            int num = sc.nextInt();
            int cnt = 0;
            for(int i = 1;;i++){
                cnt = (cnt*10+1)%num;
                if (cnt == 0) {
                    System.out.println(i);
                    break;
                }

            }
        }
    }
}