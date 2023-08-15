class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        int [] x1 = new int[10];
        int [] y1 = new int[10];
        
        for (String x : X.split("")){
            x1[Integer.parseInt(x)]++;
        }
        
        for (String y : Y.split("")){
            y1[Integer.parseInt(y)]++;
        }
        
        for (int i = 9; i >= 0; i--){
            while(x1[i] > 0 && y1[i] > 0) {
                sb.append(i);
                
                x1[i]--;
                y1[i]--;
            }
        }
        
        if("".equals(sb.toString())) return "-1";
        if("0".equals(sb.toString().substring(0,1))) return "0";
        else answer = sb.toString();
        
        return answer;
    }
}