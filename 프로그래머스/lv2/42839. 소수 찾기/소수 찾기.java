import java.util.*;
class Solution {
    HashSet <Integer> numberSet = new HashSet<>();
    
    public boolean isPrime(int num) {
        if (num == 0 || num == 1){
            return false;
        }
        int limit = (int)Math.sqrt(num); // 에라토스테네스의 체 사용 소수는 그 수의 제곱근까지만 보면 된다.
        
        for (int i =2; i <= limit; i++){
            if (num%i==0) {
                return false;
            }
        }
        return true;
    }
    public void recursive(String comb, String others) {
        if(!comb.equals("")){
            numberSet.add(Integer.valueOf(comb)); // 정수로 바꿔서 넣어주고
        }
        
        for (int i =0; i< others.length(); i++) {
            recursive(comb + others.charAt(i), others.substring(0,i) + others.substring(i+1));
            // for문 잘봐라 1 들어가고 재귀 7 들어가고 없어서 for문 종료 for문 1로 들어가서 comb ""부터 다시 시작 
        }
    }
    public int solution(String numbers) {
        recursive("", numbers);
        int count = 0;
        Iterator<Integer> it = numberSet.iterator(); // 굳이 안써도 되지만 통용되는거라서 편해서 쓴다함
        while(it.hasNext()) { // it의 다음이 있다면?
            int number = it.next(); // 다음 뽑아줘
            if (isPrime(number)){
                count++;
            }
        }
        return count;
    }
}