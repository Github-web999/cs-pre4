def find_largest_and_second_largest(nums):


    if len(nums) < 2:
        return None, None  

    max_value = nums[0]
    second_max_value = float('-inf') 

    for num in nums:
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value and num != max_value:
            second_max_value = num

    return max_value, second_max_value


nums = [0, 2, 5, 10, 3, 7, 9]
largest, second_largest = find_largest_and_second_largest(nums)
print("Số lớn nhất:", largest)
print("Số lớn thứ hai:", second_largest)