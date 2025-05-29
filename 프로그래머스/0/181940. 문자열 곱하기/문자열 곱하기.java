class Solution {
    public String solution(String my_string, int k) {
        String answer = my_string;
        for(int i = 0; i < k-1; i++){
            answer += my_string;
        }
        return answer;
    }
}