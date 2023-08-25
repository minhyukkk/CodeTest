import java.util.*;
class Solution {
    int[] dx = {-1,1,0,0};
    int[] dy = {0,0,-1,1};
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        
        boolean [][] visited = new boolean[m][n];
        
        for (int i = 0; i < picture.length; i++) {
            for (int j = 0; j < picture[0].length; j++){
                if(!visited[i][j] && picture[i][j] != 0) {
                    maxSizeOfOneArea = Math.max(
                            bfs(i, j, picture, visited, picture[i][j]), maxSizeOfOneArea);
                    numberOfArea++;
                } // 제일 큰 영역과 영역의 갯수를 세어주기 위함
            }
        }
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    public int bfs(int x, int y, int[][] graph, boolean[][] visited, int color) {
        int count = 1;
        visited[x][y] = true;
        
        Queue <int[]> q = new LinkedList<>();
        q.add(new int[] {x,y});
        
        while(!q.isEmpty()){
            int [] pop = q.remove();
            int px = pop[0];
            int py = pop[1];
            
            for (int i = 0; i < 4; i++){
                int nx = px + dx[i];
                int ny = py + dy[i];
                
                if (0 <= nx && nx < graph.length && 0 <= ny && ny < graph[0].length && !visited[nx][ny] && graph[nx][ny] == color){
                    q.add(new int[] {nx,ny});
                    visited[nx][ny] = true;
                    count++;
                }
            }
            
        }
        return count;
    }
}