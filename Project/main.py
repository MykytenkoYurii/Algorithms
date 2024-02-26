import random
import time

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def choose_sort(arr):
    start_time = time.time()
    for el in range(len(arr)):
        min_el = el
        for j in range(el+1, len(arr)):
            if arr[j] < arr[min_el]:
                min_el = j
        arr[el], arr[min_el] = arr[min_el], arr[el]
    end_time = time.time()
    return arr, end_time - start_time

def bubble_sort(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time

size = get_int_input("\nВведіть розмір масиву: ")
arr = [random.randint(0, 100) for _ in range(size)]

choose = get_int_input("\nЯк ви хочете відсортувати масив (1 - Сортування вибором, 2 - Бульбашкове сортування): ")

if choose == 1:
    sorted_arr, sort_time = choose_sort(arr)
    print("\nМасив відсортований методом вибору:", sorted_arr)
    print(f"Час виконання сортування: {sort_time} секунд")
elif choose == 2:
    sorted_arr, sort_time = bubble_sort(arr)
    print("\nМасив відсортований бульбашковим сортуванням:", sorted_arr)
    print(f"Час виконання сортування: {sort_time} секунд")
else:
    print("\nНевідомий метод сортування.")
