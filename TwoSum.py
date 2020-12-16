

def twoSum(nums, target):
    answer = nums
    for x in reversed(answer):
        if x > target:
            answer.remove(x)


    print(answer)


nums_in = [2, 7, 11, 15]
target_in = 9

twoSum(nums_in, target_in)