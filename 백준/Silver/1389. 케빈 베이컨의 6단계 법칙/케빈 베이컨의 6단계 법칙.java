// 보자마자 DFS라고 생각 -> LIST에 1 -> 3,4 이런 식으로 다 넣고 VISITED 표시하면서 가면 될줄 -> 내가 얼추 생각했던게 BFS였다..?
// 허나 2주 간의 공백으로 인해......... 구현도 못해버림


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n,m;
    static int[] dis, visited;
    static List<Integer>[] list;
    static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dis = new int[n+1];
        list = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            list[a].add(b);
            list[b].add(a);
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                check = new boolean[n + 1];
                visited = new int[n + 1];

                if (i != j) {
                    int result = bfs(i, j);
                    dis[i] += result; // i가 모든 친구와 만나려면을 계산
                }
            }
        }

        int min = Integer.MAX_VALUE;
        int idx = 0;
        for (int i = 1; i <= n; i++) {
            if(min > dis[i]){
                min = dis[i];
                idx = i;
            }
        }
        System.out.println(idx);
    }

    static int bfs(int i, int j){
        Queue<Integer> q = new LinkedList<>();
        q.add(i);
        check[i] = true;

        while(!q.isEmpty()) {
            int su = q.poll();

            if(su == j) {
                return visited[su]; // i와 j가 연결되려면 몇번을 해야하는지 갯수 반환
            }
            for (int k = 0; k < list[su].size(); k++) { // 현재 가져온 것과 어떤 것이 이어져 있는지 확인하면서
                int next = list[su].get(k);
                if(!check[next]){
                    check[next] = true;
                    q.add(next);
                    visited[next] = visited[su] +1;
                }
            }
        }
        return 0;
    }
}
