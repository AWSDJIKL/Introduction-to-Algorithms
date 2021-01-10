import math


# 归并排序
def merge_sort(list, start, end):
    if start == end:
        return
    mid = start + ((end - start) // 2)
    merge_sort(list, start, mid)
    merge_sort(list, mid + 1, end)
    merge(list, start, mid, end)
    return


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    left.append(math.inf)
    right.append(math.inf)
    for i in range(end - start):
        if left[0] <= right[0]:
            list[start + i] = left.pop(0)
        else:
            list[start + i] = right.pop(0)
    return


test_list = [3, 5, 1, 9, 6]
merge_sort(test_list, 0, 5)
print(test_list)
