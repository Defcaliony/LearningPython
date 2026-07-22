#Списки з даними

nums = [5, 7, 4, 5.45, 6]
nums[0] = 34.34
#print(nums[3])


nums2 = [5, 7, 3,[5, "Text", True, ]]
#print(nums2[-2])

nums.append(45)
nums.insert(1, False) #False =0, True = 1
# nums.extend(nums2)
nums.sort()
nums.reverse()
#nums.pop()
nums.remove(34.34)
#nums.clear


print(nums)
print(nums.count(6))
print(len(nums))