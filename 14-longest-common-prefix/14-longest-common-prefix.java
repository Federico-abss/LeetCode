class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int i = 0;
        while (true) {
            char curChar = 'A';
            for (String str : strs) {
                if (str.length() <= i) {
                    return strs[0].substring(0, i);
                }
                if (curChar == 'A') {
                    curChar = str.charAt(i);
                } else if (curChar != str.charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
            i++;
        }
    }
}