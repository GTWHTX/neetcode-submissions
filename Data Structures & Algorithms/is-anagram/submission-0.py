class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = dict()
        for symbol in s:
            my_dict[symbol] = my_dict.get(symbol, 0) + 1
        for symbol in t:
            if symbol not in my_dict or my_dict[symbol] == 0:
                return False
            my_dict[symbol] -= 1
        return True