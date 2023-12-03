#для бинарного поиска использую структурную и процедурную парадигмы

from typing import List
from random import randint


def binary_search(arr: List[int], item: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    # массив, в котором будет производиться поиск
    arr = [randint(1, 50) for i in range(10)]

    print(f"Исходный массив: {arr}")
    item = int(input("Введите искомый элемент: "))
    result = binary_search(arr, item)

    if result == -1:
        print("Элемент в массиве отсутствует")
    else:
        print(f"Элемент: {item} имеет индексу: {result}")


if __name__ == "__main__":
    main()
