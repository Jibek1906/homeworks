def selection_sort(unsorted):
    n = len(unsorted)

    for i in range(n):
        min_element_index = i
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_element_index]:
                min_element_index = j
        unsorted[i], unsorted[min_element_index] = unsorted[min_element_index], unsorted[i]
    return unsorted


def binary_search(Val, A):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Val:
            ResultOk = True
            Pos = Middle
            break
        elif A[Middle] < Val:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print("Элемент найден")
        print("Pos:", Pos)
    else:
        print("Элемент не найден")


unsorted_list = [23, 45, 1, 3, 12, 7, 5, 19]

sorted_list = selection_sort(unsorted_list)

print(sorted_list)

print("Sorted list:", sorted_list)

binary_search(19,sorted_list)
