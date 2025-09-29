def solve(n):
    def _solve(row, columns, diag1, diag2):
        if row == n:
            return 1
        count = 0
        available = ((1 << n) - 1) & ~(columns | diag1 | diag2)
        while available != 0:
            position = available & -available
            available -= position
            count += _solve(row + 1, columns | position, (diag1 | position) << 1, (diag2 | position) >> 1)
        return count

    return _solve(0, 0, 0, 0)


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
