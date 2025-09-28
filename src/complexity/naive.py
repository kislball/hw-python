import itertools

def check_field(queens: list[int]):
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(queens[i] - queens[j]) == j - i:
                return False
    return True

def solve(n):
    count = 0
    for perm in itertools.permutations(range(n)):
        if check_field(perm):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
