class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        win = set()
        lose = set([0])
        def solve(n):
            if n in win:
                return True
            if n in lose:
                return False
            i = 1
            while i * i <= n:
                if solve(n - i * i) == False:
                    win.add(n)
                    return True
                i += 1
            lose.add(n)
            return False

        return solve(n)