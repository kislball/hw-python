"""Переборное решение задачи с ферзями.

Перебирвет все перестановки ферзей по колонкам, проверяет каждую на наличие конфликтов.
При запуске напрямую выводит решение для числа, заданного через stdin.

Более подробное описание сложности содержится в файле complexity.md.
"""

import itertools


def check_field(queens: list[int]):
    """Проверяет наличие ферзей, атакуемых другими ферзями, на данном поле."""
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(queens[i] - queens[j]) == j - i:
                return False
    return True


def solve_naive(n):
    """Решает задачу о расположении n ферзей на шахматной доске размера n*n."""
    count = 0
    for perm in itertools.permutations(range(n)):
        if check_field(perm):
            count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    print(solve_naive(n))
