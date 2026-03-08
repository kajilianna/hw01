class QueensSolver:
    def solve(self, n):
        """
        求解 n 皇后问题，返回所有可能解法的数量
        """
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1  # 修复：row==n时应当返回1而不是0
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                count += backtrack(
                    row + 1,
                    cols | {col},
                    diag1 | {row - col},
                    diag2 | {row + col}
                )
            return count
        return backtrack(0, set(), set(), set())