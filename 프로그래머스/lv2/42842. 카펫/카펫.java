class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int x = Integer.MAX_VALUE;
        int y = Integer.MIN_VALUE;
        
        int count = brown + yellow;
        
        for (int i = count; i > 0; i--) {
            int j = 0;
            int center = 0;
            if (count % i == 0) {
                j = count / i;
                if (i < j) {
                    break;
                }
                center = (i-2) * (j-2);
                if (i < x && j > y && center == yellow){
                    x = i;
                    y = j;
                }
            }
        
        }
        answer[0] = x;
        answer[1] = y;
        return answer;
    }
}