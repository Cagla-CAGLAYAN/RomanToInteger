class Solution(object):
  def romanToInt(self, s):
      list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
      if (1 <= len(s) <= 15):
        number = 0

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        print(s)
        for char in s:
            number = number + list[char]
        return number
      else:
          print("please enter a valid roman number.")

sol = Solution()

print("enter your roman number here: ")
input = input()
decimal = sol.romanToInt(input)
print(decimal)





