import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int [] array;
    static boolean [] isSelected;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");


        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        array = new int[m];
        isSelected = new boolean[n+1];

        perm(0);
        System.out.println(sb);
    }

    private static void perm(int cnt){
        for (int i = 1; i <= n; i++) {
            if(cnt == m) {
                for (int result : array){
                    sb.append(result).append(" ");
                }
                sb.append("\n");
                return;
            }

            if(isSelected[i]) continue;

            array[cnt] = i;
            isSelected[i] = true;
            perm(cnt+1);
            isSelected[i] = false;
        }
    }

}
