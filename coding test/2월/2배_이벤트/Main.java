import java.io.*;
import java.util.StringTokenizer;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int result = 0;
		int [][] arr = new int [N][N];
		for(int i =0; i< N ;i++){
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			arr[i][0]=Integer.parseInt(st1.nextToken());
			arr[i][1]=Integer.parseInt(st1.nextToken());
		}
		Arrays.sort(arr, (o1,o2) -> (o1[0]==o2[0] ? o2[1] - o1[1] : o2[0]- o2[0] ) );
		
		for(int j = 0 ; j < N ; j++){
			if(K==0){
				result += arr[j][0]*arr[j][1];
			}else if(arr[j][1]>K){
				result += arr[j][0] *2*K;
				result += arr[j][0]*(arr[j][1]-K);
				K=0;
			}else if(arr[j][1]<K){
				result += arr[j][0] *2 *arr[j][1];
				K = K - arr[j][1];
			}else if (arr[j][1]==K){
				result += arr[j][0]*2*K;
				K=0;
			}
		}
		System.out.println(result);
	}
}