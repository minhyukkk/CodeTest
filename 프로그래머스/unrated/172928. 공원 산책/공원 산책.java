class Solution {
    public int[] solution(String[] park, String[] routes) {
        // 초기화 : S 시작
        int[] answer = new int[2];
        
        Boolean found = false;
        for(int i=0; i<park.length; i++) {
            for(int j=0; j<park[i].length(); j++) {
                if(park[i].charAt(j) == 'S') {
                    found = true;
                    answer[0] = i;
                    answer[1] = j;
                    break;
                }
            }
            if(found) {
                break;
            }
        }
        
        // 공원 크기 사전 측정
        int x = park[0].length() - 1;
        int y = park.length - 1;
        
        for(String route : routes) {
            String des = route.split(" ")[0]; // 방향 : N E W S
            Integer move = Integer.parseInt(route.split(" ")[1]); // 이동거리
            
            if("N".equals(des)) {
                // 범위 초과
                if(answer[0] - move < 0) {
                    continue;
                }
                // 장애물 여부 확인
                Boolean isBlock = false;
                for(int i=1; i<=move; i++) {
                    if(park[answer[0]-i].charAt(answer[1]) == 'X') {
                        isBlock = true;
                        break;
                    }
                }
                if(isBlock) {
                    continue;
                }
                // 전부 통과했으면 해당 위치로 이동
                answer[0] = answer[0] - move;
            }
            else if("W".equals(des)) {
                // 범위 초과
                if(answer[1] - move < 0) {
                    continue;
                }
                // 장애물 여부 확인
                Boolean isBlock = false;
                for(int i=1; i<=move; i++) {
                    if(park[answer[0]].charAt(answer[1]-i) == 'X') {
                        isBlock = true;
                        break;
                    }
                }
                if(isBlock) {
                    continue;
                }
                // 전부 통과했으면 해당 위치로 이동
                answer[1] = answer[1] - move;
            }
            else if("S".equals(des)) {
                // 범위 초과
                if(answer[0] + move > y) {
                    continue;
                }
                // 장애물 여부 확인
                Boolean isBlock = false;
                for(int i=1; i<=move; i++) {
                    if(park[answer[0]+i].charAt(answer[1]) == 'X') {
                        isBlock = true;
                        break;
                    }
                }
                if(isBlock) {
                    continue;
                }
                // 전부 통과했으면 해당 위치로 이동
                answer[0] = answer[0] + move;
            }
            else if("E".equals(des)) {
                // 범위 초과
                if(answer[1] + move > x) {
                    continue;
                }
                // 장애물 여부 확인
                Boolean isBlock = false;
                for(int i=1; i<=move; i++) {
                    if(park[answer[0]].charAt(answer[1]+i) == 'X') {
                        isBlock = true;
                        break;
                    }
                }
                if(isBlock) {
                    continue;
                }
                // 전부 통과했으면 해당 위치로 이동
                answer[1] = answer[1] + move;
            }
        }
        
        return answer;
    }
}