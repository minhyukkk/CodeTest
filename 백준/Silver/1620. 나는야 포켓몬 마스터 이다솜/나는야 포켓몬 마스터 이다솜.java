// hashmap 사용해서 비교하면 된다고 생각하고 풀려고 했으나 2주 안했다고 하나도 기억 안나는 사고 발생.
// 두번째 입력 값 받아서 하는 방법이 기억이 전혀 안남 사고 또 발생

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map <String, Integer> monster = new HashMap<String, Integer>();
        String[] monsterArr = new String[n+1];

        for(int i = 1; i <= n; i++) {
            String name = br.readLine();
            monster.put(name, i);
            monsterArr[i] = name;
        }

        for (int i = 0; i < m; i++){
            String question = br.readLine();
            if(49 <= question.charAt(0) && question.charAt(0) <= 57){
                System.out.println(monsterArr[Integer.parseInt(question)]);
            }
            else {
                System.out.println(monster.get(question));
            }
        }
    }

}
