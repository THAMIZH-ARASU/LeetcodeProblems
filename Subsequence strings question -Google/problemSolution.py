"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A sequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde"

Example 1:
Input: s = 'abcde', words = ['a', 'bb', 'acd', 'ace']
Output: 3

Example 2:
Input: s = 'dsahjpjauf', words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']
Output: 2
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        char_indices = {}
        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        def is_subsequence(word: str) -> bool:
            previous_index = -1
            for char in word:
                if char not in char_indices:
                    return False
                
                indices = char_indices[char]
                left, right = 0, len(indices)
                while left < right:
                    mid = (left + right) // 2
                    if indices[mid] > previous_index:
                        right = mid
                    else:
                        left = mid + 1
                if left == len(indices):
                    return False
                previous_index = indices[left]
            return True

        count = 0
        accepted_words = []
        for word in words:
            if is_subsequence(word):
                count += 1
                accepted_words.append(word)
        print(f"Accepted words: {accepted_words}")
        return count
    
if __name__ == '__main__':
    solution = Solution()
    s1 = 'abcde'
    words1 = ['a', 'bb', 'acd', 'ace']
    print(solution.numMatchingSubseq(s1, words1))  # Output: 3

    s2 = 'dsahjpjauf'
    words2 = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']
    print(solution.numMatchingSubseq(s2, words2))  # Output: 2