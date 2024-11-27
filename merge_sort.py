def merge_sort(arr):
    if len(arr) <= 1:
        return arr #Base case for recursion
    
    mid = len(arr)//2 #finds middle value
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:]) #uisng recursion to sort the left and right sight of the list from the middle value 
    
    return merge(left, right)

def merge(arr):
    