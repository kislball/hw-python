class EuclidResult:
    def __init__(self, gcd, bezout):
        self.bezout = bezout
        self.gcd = gcd

def extended_euclid(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quot = old_r // r
        old_r, r = r, old_r - quot * r
        old_s, s = s, old_s - quot * s
        old_t, t = t, old_t - quot * t

    return EuclidResult(gcd = old_r, bezout = (old_s, old_t))

if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    result = extended_euclid(a, b)

    print(f"НОД - {result.gcd}, коэф. Безу - {result.bezout}")

