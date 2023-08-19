import java.util.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        ArrayList<Integer> win_list = new ArrayList<>();
        ArrayList<Integer> my_list = new ArrayList<>();
        int count = 0;
        int count3 = 0;
        
        for (int num : win_nums) {
            win_list.add(num);
        }
        
        for (int num : lottos) {
            my_list.add(num);
        }
        
        for (int i = 0; i < win_nums.length; i++) {
            if (win_list.contains(my_list.get(i))) {
                count++;
            }
        }
        
        
        for (int i = 0; i<lottos.length; i++){
            if (lottos[i] == 0){
                count3++;
            }    
        }
        
        int count2 = count + count3;
        
        if (count == 6) {
            answer[1] = 1;
        }
        
        if (count == 5) {
            answer[1] = 2;
        }
        if (count == 4) {
            answer[1] = 3;
        }
        if (count == 3) {
            answer[1] = 4;
        }if (count == 2) {
            answer[1] = 5;
        }
        if (count == 1 || count == 0) {
            answer[1] = 6;
        }
        
        
        if (count2 == 6) {
            answer[0] = 1;
        }
        
        if (count2 == 5) {
            answer[0] = 2;
        }
        if (count2 == 4) {
            answer[0] = 3;
        }
        if (count2 == 3) {
            answer[0] = 4;
        }if (count2 == 2) {
            answer[0] = 5;
        }
        if (count2 == 1 || count2 == 0) {
            answer[0] = 6;
        }
        
        
        return answer;
    }
}