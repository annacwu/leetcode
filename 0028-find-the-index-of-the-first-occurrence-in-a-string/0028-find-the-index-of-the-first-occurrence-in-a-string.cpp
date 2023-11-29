class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = needle.length();
        for (int i = 0; i < haystack.length(); i++){
            if (haystack[i] == needle[0]){
                string check = haystack.substr(i,n);
                if (check == needle){
                    return i;
                }
            }
        }
        return -1;
    }
};