// bfs 쓸 생각도 x 알고리즘이 아닌 어떠한 규칙이 있을거라고 생각했지만...
// 문제가 너비우선탐색 이라는 말 그대로 생각하면 됨

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n;
    static int k;
    static int isVisited[] = new int[100001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        String [] inputs = input.split(" ");

        n = Integer.parseInt(inputs[0]);
        k = Integer.parseInt(inputs[1]);

        int result = bfs();
        System.out.println(result);
    }
    private static int bfs() {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(n);
        isVisited[n] = 1;

        while (q.isEmpty() == false){
            int su = q.remove();
            if (su == k) {
                return isVisited[su] - 1;
            }
            if (su-1 >=0 && isVisited[su-1] == 0){
                isVisited[su-1] = isVisited[su] +1;
                q.add(su-1);
            }
            if (su+1 <= 100000 && isVisited[su+1] == 0) {
                isVisited[su+1] = isVisited[su]+1;
                q.add(su+1);
            }
            if(2*su <= 100000 && isVisited[2*su] == 0){
                isVisited[2*su] = isVisited[su] +1;
                q.add(2*su);
            }
        }
        return -1;
    }




}
