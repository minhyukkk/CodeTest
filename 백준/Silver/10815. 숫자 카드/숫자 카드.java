import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int [] array = new int[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {

            array[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        int [] array2 = new int[M];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < M; i++) {
            array2[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(array);

        for (int i = 0; i < M; i++) {
            sb.append(card(array, array2[i])).append(" ");
        }

        System.out.println(sb);
    }

    public static int card(int[] array, int key){
        int low = 0;
        int high = array.length - 1;
        int mid;

        while(low <= high) {
            mid = (low + high) / 2;
            if (key == array[mid]) {
                return 1;
            }
            if (key > array[mid]) {
                low = mid + 1;
            }
            if (key < array[mid]) {
                high = mid -1;
            }
        }
        return 0;
    }
}
