"""
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check if the input string is empty, return an empty string if so
        if not s:
            return ""

        # Initialize variables to store the indices of the longest palindrome found
        longest_palindrome_indices = [0, 0]

        def expand_around_center(s, i, j):
            # Helper function to find and return the indices of the longest palindrome
            # extended from s[i..j] (inclusive) by expanding around the center
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return [i + 1, j - 1]

        for i in range(len(s)):
            current_indices = expand_around_center(s, i, i)

            # Compare the length of the current palindrome with the longest found so far
            if current_indices[1] - current_indices[0] > longest_palindrome_indices[1] - longest_palindrome_indices[0]:
                longest_palindrome_indices = current_indices

            if i + 1 < len(s) and s[i] == s[i + 1]:
                even_indices = expand_around_center(s, i, i + 1)

                # Compare the length of the even-length palindrome with the longest found so far
                if even_indices[1] - even_indices[0] > longest_palindrome_indices[1] - longest_palindrome_indices[0]:
                    longest_palindrome_indices = even_indices

        # Extract and return the longest palindrome substring using the indices
        return s[longest_palindrome_indices[0]:longest_palindrome_indices[1] + 1]
