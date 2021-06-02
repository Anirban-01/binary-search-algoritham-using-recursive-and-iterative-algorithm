# binary search using iterative method
# base case if target element in array then return value, else return -1


def binary_search1(arr, left_element, right_element, n):
    """base case"""
    while right_element >= left_element:
        mid_element = left_element + (right_element - left_element) // 2

        # algorithm1: check if target element present in middle index element then return middle element itself
        if arr[mid_element] == n:
            return mid_element

        # algorithm2: check if target element is less then middle index element then return target element present in
        # left sub array
        elif arr[mid_element] > n:
            return binary_search1(arr, left_element, mid_element - 1, n)
        # algorithm3: check if target element is greater then middle index element then return target element present in
        # right sub array
        else:
            return binary_search1(arr, mid_element + 1, right_element, n)

    return -1


arr = [0, 2, 4, 6, 8, 10]

n = int(input('enter target element:'))

result = binary_search1(arr, 0, len(arr) - 1, n)

if result != -1:
    print('result:', str(result))
else:
    print('element not available:', -1)


# -------------------------------------------------------------------------------------------------------------------#

# if element x or target element in list of array then return value, else return -1
# base_case= r >= l, return middle element(l+(r-l)//2) in array


def binary_search(arr, left_element, right_element, n):
    """recursive method"""
    # base case
    if right_element >= left_element:
        mid_element = left_element + (right_element - left_element) // 2
        # Algorithm 1) if x is equal to middle element in array then return middle element
        if arr[mid_element] == n:
            return mid_element
        # Algorithm 2) if x is less then middle element in array then target element on left sub-array,
        # right_element=(mid-1)
        elif arr[mid_element] > n:
            return binary_search(arr, left_element, mid_element - 1, n)
        # Algorithm 3) if x is greater then middle element in array then target element on right sub-array,
        # left_element=(mid+1)
        else:
            return binary_search(arr, mid_element + 1, right_element, n)
    # when target element not in array then return -1
    else:
        return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input('enter number:'))

result = binary_search(arr, 0, len(arr) - 1, n)

if result != -1:
    print('result', str(result))
else:
    print('nothing', -1)
