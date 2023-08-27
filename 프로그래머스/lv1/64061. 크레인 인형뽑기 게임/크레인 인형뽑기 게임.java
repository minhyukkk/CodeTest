// 처음에 자꾸 board를 세로로 풀려고 노력함 그래서 안굴러감
// 문제 그대로 확인하면 됐음

import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack <Integer> stack = new Stack<>();
        stack.add(0);
        
        for (int move : moves){
            for (int i = 0; i < board.length; i++){
                if (board[i][move-1] != 0) {
                    if (stack.peek() == board[i][move-1]) {
                        stack.pop();
                        answer += 2;
                    }
                    else{
                        stack.push(board[i][move-1]);
                    }
                    board[i][move - 1] = 0; // 뽑았으니까 0으로 만들어 주고
                    break; // 다음 move로 이동
                }
            }   
        }
        return answer;
    }
}