arr = list(map(int, input().split()))

# Сортировка выбором
# Находим минимальный элемент и меняем с первым элементом. Затем повторяем до конца списка
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Индекс минимального элемента неотсортированной части
        for j in range(i + 1, n): # Проходим по неотсортированной части, ищем минимальный элемент
            if arr[j] < arr[min_index]:
                min_index = j
        # Или min(arr[i+1:])

        arr[i], arr[min_index] = arr[min_index], arr[i] #Меняем первый неотсортированный с минимальным
  return arr
    
    
print(' '.join(list(map(str, selection_sort(arr)))))
