import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] array = new String[numbers.length];
        
        for (int i =0; i < numbers.length; i++) {
            array[i] = String.valueOf(numbers[i]); // string으로 변환
        }
        
        Arrays.sort(array, (o1,o2) -> (o2+o1).compareTo(o1+o2));
        // 이게 역순
        
        if (array[0].equals("0")){
            return "0";
        } // 첫 시작이 0이면 바로 리턴 0
        
        for (int i =0; i<array.length; i++) {
            answer = answer + array[i];
        }
        return answer;
    }
}