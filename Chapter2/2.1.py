# 插入排序
def insertion_sort(list, reverse=False):
    result = [list[0]]
    for i in range(1, len(list)):
        key = list[i]
        for j in range(len(result)):
            if bool((result[j] < key) - reverse):
                continue
            else:
                result.insert(j, key)
                break
        else:
            result.append(key)
    return result


test_list = [3, 2, 5, 1, 6]
print(insertion_sort(test_list, False))
print(insertion_sort(test_list, True))
