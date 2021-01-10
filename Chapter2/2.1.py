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

# 2.1-3 线性查找
def linear_search(list,v):
    result = None
    for i in range(len(list)):
        if list[i] == v:
            result = i
            return result
    return result


test_list = [3, 2, 5, 1, 6]
print(insertion_sort(test_list, False))
print(insertion_sort(test_list, True))
