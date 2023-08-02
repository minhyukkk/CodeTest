// class Solution {
//     public boolean solution(String[] phone_book) {
//         boolean answer = true;
//         for (int i = 0; i < phone_book.length; i++) {
//             for (int j = i+1; j < phone_book.length; j++) {
//                 if (phone_book[i].contains(phone_book[j]) || phone_book[j].contains(phone_book[i])){
//                     answer = false;
//                     return answer;
//                 }
//             }
//         }
//         return answer;
//     }
// }

import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap <String, Integer> map = new HashMap<>();
        
        for(int i =0; i < phone_book.length; i++) {
            map.put(phone_book[i], 1);
            // phone_book의 내용을 map에 하나씩 넣는다 value 값을 필요 없기 때문에 1로 통일
        }
        
        for (int i =0; i < phone_book.length; i++) {
            for (int j = 1; j < phone_book[i].length(); j++) {
                if(map.containsKey(phone_book[i].substring(0,j))){
                    // 하나씩 돌아가면서 확인한다 단순히 확인하는 것이 아닌 문자열을 하나씩 늘리면서
                    answer = false;
                    return answer;
                }
            }
        }
        return answer;
    }
}