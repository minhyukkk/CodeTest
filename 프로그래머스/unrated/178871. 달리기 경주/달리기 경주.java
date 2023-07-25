import java.util.Map;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> rank = new HashMap<>();
//         Map 키, 값 순서
        for(int i = 0; i < players.length; i++) {
            rank.put(players[i], i);
        }
        
        for(String player:callings){
            int ownRank = rank.get(player);
//          rank의 player에 맞는 키 값을 가져온다 여기서 키 값은 숫자(등수)
            String beforePlayer = players[ownRank-1];
            
            players[ownRank-1] = player;
            players[ownRank] = beforePlayer;
            
            rank.put(player, ownRank-1);
            rank.put(beforePlayer, ownRank);
        }
        return players;
    }
}