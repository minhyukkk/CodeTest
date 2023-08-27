import java.util.*;

class Solution {
    int[] dx = {-1,1,0,0};
    int[] dy = {0,0,-1,1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        int[][] isVisited = new int [maps.length][maps[0].length];
        isVisited[0][0] = 1;
        bfs(0,0, isVisited, maps);
        
        answer = isVisited[maps.length-1][maps[0].length-1];
        
        if (answer == 0) answer = -1;
        return answer;
    }
    
    public void bfs(int a, int b, int isVisited[][], int maps[][]) {
        Queue <int[]> q = new LinkedList<>();
        q.add(new int[]{a,b});
        
        while (!q.isEmpty()){
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];
            
            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length && isVisited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    
                    isVisited[nx][ny] += isVisited[x][y] +1;
                    q.add(new int[]{nx,ny});

                }
            }   
        }
    }
}