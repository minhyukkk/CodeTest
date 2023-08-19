import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map <String, HashSet<String>> map = new HashMap<>();
        Map<String, Integer> index = new HashMap<>();
        // 맨 앞에 HashMap이나 Map이나 같음 하지만 Map으로 선언하는게 좀 더 안정적이다.
        // <.., HashSet<String>>으로 선언시 밑에 보면 똑같은 사람이 재신고 하는걸 막기 위해 중복 제거
        
        for (int i =0; i < id_list.length; i++) {
            String name = id_list[i];
            map.put(name, new HashSet<>()); // 일단 name만 넣고 hashset을 만들어 놓음
            index.put(name, i); // index에는 name과 i를 넣는 이유는 인덱스 값을 넣어서 answer에서 값을 추가하는게 훨씬 편함
        }
        
        for (String r : report) {
            String[] str = r.split(" ");
            String from = str[0];
            String to = str[1];
            map.get(to).add(from); // 내가 몇번 신고 당했는지를 알 수 있음
        }
        
        for (int i = 0; i < id_list.length; i++){
            HashSet<String> send = map.get(id_list[i]);
            if (send.size() >= k) {
                for (String s : send) {
                    answer[index.get(s)]++;
                }
            }
        }
        return answer;
    }
}