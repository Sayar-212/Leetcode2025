class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                new_str += word1[i]
            if i < len(word2):
                new_str += word2[i]
        return new_str
