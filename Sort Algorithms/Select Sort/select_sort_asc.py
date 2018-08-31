'''选择排序，升序'''

def selection_sort(L):
    n = len(L)
    for i in range(n-1):  # 共需要n-1次选择操作
        min_index = i  # 首先假设 "未排序列表"(上图中非绿色框) 的最小元素是它的第1个元素，第1次选择操作则假设L[0]是最小的，第2次操作则假设L[1]是最小的

        for j in range(i+1, n):  # 找出 "未排序列表" 中真正的最小元素的下标
            if L[j] < L[min_index]:
                min_index = j

        if min_index != i:  # 如果 "未排序列表" 中真正的最小元素，不是之前假设的元素，则进行交换
            L[i], L[min_index] = L[min_index], L[i]

L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('Before: ', L1)
selection_sort(L1)
print('After: ', L1)

# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
