def solve(n):
    def _solve(row, queens):
        if row == n:
            return 1
        count = 0
        for i in range(n):
            if i not in queens and all(abs(i - c) != abs(r - row) for r, c in enumerate(queens)):
                count += _solve(row + 1, queens + [i])
        return count
    return _solve(0, [])

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
