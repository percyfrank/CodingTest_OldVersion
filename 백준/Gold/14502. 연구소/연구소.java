import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static class virus {
        int x,y;

        public virus(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static int N;
    static int M;
    static int[][] map;
    static int[][] c_map;

    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int ans = Integer.MIN_VALUE;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        map = new int[N][M];
        c_map = new int[N][M];

        for(int i = 0; i < N; i++) {
            for(int j = 0;j < M; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        c_map = map;

        wall(0);

        System.out.println(ans);

    }
    public static void wall(int cnt) {

        if (cnt == 3){
            bfs();
            return;
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 1;
                    wall(cnt+1);
                    map[i][j] = 0;
                }
            }
        }
    }
    public static void bfs() {

        int[][] virus = new int[N][M];
        Queue<virus> queue = new LinkedList<virus>();

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                virus[i][j] = map[i][j];
            }
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                // 바이러스 이면 큐에 넣음
                if (virus[i][j] == 2) {
                    queue.add(new virus(i,j));
                }
            }
        }

        while(!queue.isEmpty()) {

            virus v = queue.remove();

            for(int i = 0; i < 4; i++){
                int nx = v.x + dx[i];
                int ny = v.y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    // 빈칸이면 바이러스로 바꾸고 다시 큐에 넣기
                    if (virus[nx][ny] == 0) {
                        virus[nx][ny] = 2;
                        queue.add(new virus(nx,ny));
                    }
                }
            }
        }
        safe(virus);
    }
    public static void safe(int[][] virus) {

        int cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (virus[i][j] == 0) cnt++;
            }
        }
        ans = Math.max(cnt, ans);
    }
}