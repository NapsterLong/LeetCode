def heap_sort(arr):
    length = len(arr)

    for i in range(length - 1, -1, -1):
        adjust(arr, length, i)

    for i in range(length - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        adjust(arr, i, 0)


def adjust(arr, length, i):
    temp = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < length and arr[left] > arr[i]:
        temp = left

    if right < length and arr[right] > arr[temp]:
        temp = right

    if temp != i:
        arr[i], arr[temp] = arr[temp], arr[i]
        adjust(arr, length, temp)


arrs = [5, 6, 13, 12, 11, 7]
heap_sort(arrs)
print(arrs)
