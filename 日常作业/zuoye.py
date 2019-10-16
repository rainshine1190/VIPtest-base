#coding:utf-8
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

nums = [2,7,11,15,0,9]
target = 9

for j in range(len(nums)):
    for i in range(j+1,len(nums)):
        print('两值相加：',nums[j],nums[i])
        sum = nums[j] + nums[i]
        if sum == target:
            print('下标为--：',j,i)




