class Solution {
    public int solution(String s) {
        int answer = 0;
        char c = s.charAt(0);
        int count1 = 0;
        int count2 = 0;
        
        for (int i =0; i < s.length(); i++) {
            if(count1 == count2) {
                answer++;
                c = s.charAt(i);
            }
            
            if (c == s.charAt(i)) {
                count1++;
            }
            else {
                count2++;
            }
            
        }
        return answer;
    }
}