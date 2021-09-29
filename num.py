
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n/4!=0
if __name__ == '__main__':
    print(Solution.canWinNim(4, 5))