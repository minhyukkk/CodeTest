import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap <String, Integer> map = new HashMap<>(); // 어차피 갯수만 출력해주기 때문에 Integer
        
        for (int i =0; i < clothes.length; i++){
            String type = clothes[i][1];
            map.put(type, map.getOrDefault(type, 0) +1); // map에 type 값이 없으면 0 있으면 +1
        }
        
        Iterator<Integer> it = map.values().iterator();
        while(it.hasNext()){ // 다음 값이 있다면
            answer *= it.next().intValue() +1; // 다음 값을 int형으로 바꾸고 입지 않은 경우를 생각하여 +1
        }
        
        answer -= 1; // 전부 다 입지 않은 경우를 빼기 위해 -1
        return answer; 
    }
}