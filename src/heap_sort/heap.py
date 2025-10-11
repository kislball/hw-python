def heapify(arr, n, i):
    """Превращение поддерева с корнем в узле i(индекс в массиве arr)"""
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        heapify(arr, n, largest)

def heap_sort(arr):
    """Сортировка кучей"""
    n = len(arr) 

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)

if __name__ == "__main__":
    data = input("Введите числа через пробел: ")
    array = [int(x) for x in data.split(' ')]
    heap_sort(array)
    print(' '.join(str(x) for x in array))
