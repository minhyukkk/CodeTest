import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue <Integer> q = new PriorityQueue<>();
        // 우선순위 큐는 힙의 성질을 이용 먼저 들어온 것이 빠지는게 아닌 값이 작은 것이 먼저 빠짐
        
        for (int i = 0; i < scoville.length; i++) {
            q.add(scoville[i]); // push 안된다
        }
        
        while (q.peek() < K) { // 맨위에꺼가 빠지니까 그게 k보다 크면은 종료
            if (q.size() == 1) return -1;
            q.add(q.poll() + q.poll() * 2);
            answer += 1;
        }
        return answer;
    }
}