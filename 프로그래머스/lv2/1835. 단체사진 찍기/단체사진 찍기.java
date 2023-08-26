class Solution {
    private int answer = 0;
    private String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};
    
    public int solution(int n, String[] data) {
        boolean[] isVisited = new boolean[8];
        dfs("", isVisited, data);
        return answer;
    }
    
    public void dfs(String names, boolean[] isVisited, String[] datas) {
        if (names.length() == 7) {
            if (check(names, datas)){ // check를 이용해서 return이 true라면 맞는거니까 ++
                answer++;
            }
            return;
        }
        for (int i =0; i < 8; i++){ // 이 과정을 통해 A 부터 정렬을 해주는거임
// return이 된다면 다시 이제 B부터 차례대로 쫙 정렬을 해주는 for문
            if(!isVisited[i]){
                isVisited[i] = true;
                String name = names + friends[i];
                dfs(name, isVisited, datas); 
                isVisited[i] = false; // 다시 처음부터 돌아야 하니 dfs 끝나면 visited false로
            }
        }
    }
    
    public boolean check(String names, String[] datas){
        for(String data : datas){ // data를 하나씩 짤라서 계산한다...
            int position1 = names.indexOf(data.charAt(0));
            int position2 = names.indexOf(data.charAt(2));
            
            char op = data.charAt(3);
            int index = data.charAt(4) - '0'; // 문자이기 때문에 문자 0의 아스키코드 값을 빼서 정수로 변환
            
            if(op == '='){
                if(!(Math.abs(position1 - position2) == index+1)) return false;
            } else if (op == '>'){
                if(!(Math.abs(position1 - position2) > index+1)) return false;
            } else if (op == '<'){
                if(!(Math.abs(position1 - position2) < index+1)) return false;
            }
        }
        return true;
    }
    
}