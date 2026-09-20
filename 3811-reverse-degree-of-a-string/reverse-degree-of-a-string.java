class Solution {
    public int reverseDegree(String s) {
        int sum=0;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);

            int reverse_val = 26 - (c-'a');
            int position = i+1;

            sum += reverse_val * position;
        }
        return sum;
    }
}