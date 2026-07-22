# minimal element definition(function)
def minimal(l):
    min_num = l[0]  # min
    for i in l:
        if i < min_num:
            min_num = i

    return min_num


nums1 = [5, 3, 7, 3, -6, 6, 0, -2, 5]
res1 = minimal(nums1)

nums2 = [5, 3, 7, 3, 6, -10, 0, -2, 5]
res2 = minimal(nums2)

if res1 < res2:
    print(res1)
else:
    print(res2)
