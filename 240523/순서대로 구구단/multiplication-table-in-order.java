import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        if (a <= b) { // a가 b보다 작거나 같으면
            // 순서대로 구구단 계산
            for (int i = a; i <= b; i++) {
                gugudan(i, sb);
            }
        } else { // b가 a보다 작으면
            // 역순으로 구구단 계산
            for (int i = a; i >= b; i--) {
                gugudan(i, sb);
            }
        }

        System.out.println(sb);
    }

    // 구구단 함수
    private static void gugudan(int num, StringBuilder sb) {
        for (int i = 1; i <= 9; i++) {
            sb.append(num).append(" * ").append(i).append(" = ").append(num * i).append("  ");

            // i가 3으로 나눈 나머지가 0이면 개행
            if (i % 3 == 0) {
                sb.append("\n");
            }
        }

        sb.append("\n");
    }
}