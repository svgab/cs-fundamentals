lst = list(map(int, input().split()))


def bubble_sort(arr):
    n = len(arr) # Длина списка
    for x in range(n): # Проходимся по списку
        for y in range(0, n - x - 1): # Проходимся от нуля n - x - 1 (неотсортированное кол-во элементов - 1 для диапазона)
            if arr[y] > arr[y + 1]: # Если элемент больше следующего, свапаем их
                arr[y], arr[y + 1] = arr[y+1], arr[y] 
    return arr

print(' '.join(list(map(str, bubble_sort(lst)))))
