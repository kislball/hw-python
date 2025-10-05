"""Рекурсивное решение задачи с ферзями.

Перебирвет все перестановки ферзей по колонкам, но при этом отсекает лишние раньше,
чем наивный алгоритм.
При запуске напрямую выводит решение для числа, заданного через stdin.

Более подробное описание сложности содержится в файле complexity.md.
"""


def solve_recursive(n):
    """Решает задачу о расположении n ферзей на шахматной доске размера n*n."""

    def _solve(row, queens):
        if row == n:
            return 1
        count = 0
        for i in range(n):
            if i not in queens and all(
                abs(i - c) != abs(r - row) for r, c in enumerate(queens)
            ):
                count += _solve(row + 1, queens + [i])
        return count

    return _solve(0, [])


if __name__ == "__main__":
    n = int(input())
    print(solve_recursive(n))
