import java.io.*;
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new 	InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int caseNum = Integer.parseInt(st.nextToken());
		int[] box = new int[N];
		for(int i=0;i<caseNum;i++){
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int boxnum = Integer.parseInt(st1.nextToken());
			int sign = Integer.parseInt(st1.nextToken());
			int ball = Integer.parseInt(st1.nextToken());
			if (sign==1){
				box[boxnum-1]+=ball;
			}else{
				if(box[boxnum-1]>=ball){
					box[boxnum-1]-=ball;
				}
			}
		}
		for(int j=0;j<N;j++){
			System.out.println(box[j]);
		}
	}		
}