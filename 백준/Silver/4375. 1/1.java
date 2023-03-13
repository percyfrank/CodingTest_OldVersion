import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {

            int n = sc.nextInt();
            int idx = 0;

            for (int cnt = 1; ; cnt++) {

                // % 연산은 *, +에서 분배법칙 성립
                idx = (idx*10+1) % n;

                if (idx == 0) {
                    System.out.println(cnt);  //자릿수 출력
                    break;
                }
            }
        }
    }
}