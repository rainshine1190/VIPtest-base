

# for i in range(1,3):
#     for j in range(3):
#         print((i,j))
#
#
# list1 = [(i,j) for i in range(1,3) for j in range(3)]
# print(list1)

#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s
#
#         def expand(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]
#
#         result = ""
#         for i in range(len(s)):
#             # 处理奇数长度的回文子串
#             palindrome = expand(i, i)
#             if len(palindrome) > len(result):
#                 result = palindrome
#
#             # 处理偶数长度的回文子串
#             palindrome = expand(i, i + 1)
#             if len(palindrome) > len(result):
#                 result = palindrome
#
#         return result
#
# Solution().longestPalindrome('aba')

#需求：递归

def fun(num):
    if num == 1:
        return 1
    else:
        return num + fun(num-1)

print(fun(100))



