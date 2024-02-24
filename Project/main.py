#Check integer input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
#Check array input
def get_array_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            arr_str = user_input.split()
            return [int(number) for number in arr_str]
        except ValueError:
            print("Будь ласка, введіть числа, розділені пробілами.")
#Algorithm for choose sort
def choose_sort(arr):
    for el in range(len(arr)):
        min_el = el
        for j in range(el+1, len(arr)):
            if arr[j] < arr[min_el]:
                min_el = j
        arr[el], arr[min_el] = arr[min_el], arr[el]
    return arr
#Algorithm for bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#Input data
arr = get_array_input("\nВведіть елементи масиву через пробіл: ")
choose = get_int_input("\nЯк ви хочете відсортувати масив (1 - Сортування вибором, 2 - Бульбашкове сортування): ")
#Output 
if choose == 1:
    sorted_arr = choose_sort(arr)
    print("\nМасив відсортований методом вибору:", sorted_arr)
elif choose == 2:
    sorted_arr = bubble_sort(arr)
    print("\nМасив відсортований бульбашковим сортуванням:", sorted_arr)
else:
    print("\nНевідомий метод сортування.")
