import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet <Integer> set = new HashSet<>();
        
        
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }
        ArrayList<Integer> array = new ArrayList<>(set);
        
        Collections.sort(array); // hashset의 소트 방법은 collections 사용 하기 위해 arraylist 선언 후 넣어줌
        int[] result = array.stream().mapToInt(Integer::intValue).toArray(); // arraylist를 int로 변환해주는 것
        return result;
    }
}