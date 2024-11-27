def merge_sort(arr): # this function will sort a list of numbers in ascending order
    if len(arr) <= 1:
        return arr #Base case for recursion
    
    mid = len(arr)//2 #finds middle value
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:]) #using recursion to sort the left and right sight of the list from the middle value 
    
    return merge(left, right)

def merge(left, right): # merges the two sorted list into one ordered list
    sorted_array = []
    x = 0 #index counter for left side of list
    y = 0 #index counter for right side of list
    
    while x < len(left) and y < len(right):
        if left[x] <= right[y]:
            sorted_array.append(left[x]) #adds smallest elemnt from the left list
            x += 1
        else:
            sorted_array.append(left[y]) #adds smallest elemnt from the right list
            y += 1
    return sorted_array