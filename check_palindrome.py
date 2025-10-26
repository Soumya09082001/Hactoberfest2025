class Solution:
      def isPalindrome(Self, x: int) -> bool:
      # Negative numbers are not palindrome
      if x < 0:
        return False

      # Convert integer to string and compare with its reverse
      s = str(x)
      return s == s[::-1]
