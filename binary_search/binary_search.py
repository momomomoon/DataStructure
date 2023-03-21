##이진탐색 O(logn)
def binary_search(my_list, item):
    low = 0 
    high = len(my_list) - 1 
    
    while low <= high:
        mid = (low + high) // 2 #3.x 버전 표시법 2[5]
        guess = my_list[mid]

        if guess == item: #추측 숫자를 찾다. 
            return mid
        if guess > item: #추측 숫자가 크다. 
            high = mid - 1 # 
        else: #추측 숫자가 너무 작다. 
            low = mid + 1 
    return None #없을때

my_list = [1, 3, 5, 7, 9, 10]
print(binary_search(my_list, 9)) # -> 4
print(binary_search(my_list, 4)) # -> None
