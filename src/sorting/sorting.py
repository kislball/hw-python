# Функция сортирует список in-place
def sort(ls):
    for i in range(len(ls)):
        swap = False

        for j in range(0, len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                swap = True

        if not swap:
            break

if __name__ == "__main__":
    list_len = int(input("Введите длину списка: "))
    ls = []

    for i in range(list_len):
        ls.append(int(input(f"Введите элемент номер {i + 1}: ")))

    sort(ls)

    print(' '.join(str(x) for x in ls))

