'''
THUẬT TOÁN TÌM KIẾM
'''

#? Tìm kiếm tuyến tính (Linear Search)

'''
    @params: input_arr, target
    - input_arr: mảng cần duyệt
    - target: giá trị mình muốn tìm kiếm
'''
def linear_search(input_arr, target):
    for item in input_arr:
        if item == target:
            return item

numbers = [1, 10, 7, 30, 22, 25, 18, 6, 9, 12]
target = int(input("Nhập số để tìm kiếm: "))

result = linear_search(numbers, target)

if result:
    print(f"Tìm thấy số: {target}")
else:
    print(f"Không tìm thấy số: {target}")
    
