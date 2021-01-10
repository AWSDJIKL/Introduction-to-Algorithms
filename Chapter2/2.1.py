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
def linear_search(list, v):
    result = None
    for i in range(len(list)):
        if list[i] == v:
            result = i
            return result
    return result


# 2.1-4 n维二进制数相加
def binary_addition(a1, a2):
    result = [0]
    for i in range(len(a1) - 1, -1, -1):
        # 进位
        carry = (a1[i] + a2[i] + result[0]) // 2
        # 当前位的值
        value = (a1[i] + a2[i] + result[0]) % 2
        result[0] = value
        result.insert(0, carry)
    return result


test_list = [3, 2, 5, 1, 6]
test_binary1 = [1,1]
test_binary2 = [1,0]
print(insertion_sort(test_list, False))
print(insertion_sort(test_list, True))
print(linear_search(test_list, 5))
print(binary_addition(test_binary1, test_binary2))
