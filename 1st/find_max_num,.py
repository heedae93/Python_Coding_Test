# [-1,2,3,5,6,88,77,4] 이 배열중에서 가장 큰수를 찾는다.


def find_max_num1(arr):
    for number in arr:
        is_max_num = True
        for compare_number in arr:
            if number < compare_number:
                is_max_num = False
        if is_max_num:
            print(number)
            return number



def find_max_num2(arr):
    max_number = arr[0]
    for number in arr:
        if max_number < number:
            max_number = number
    return max_number

find_max_num1([3,2,1,4,5,-1]) # 5
find_max_num1([3,2,1,4,5,-1]) # 5