
# Find the kth smallest element in an array
# using quickselect algorithm
# complexity O(n) on average, O(n^2) in worst case(time complexity)

def quick_select(arr,k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr)//2]
    
    left = [x for x in arr if x<pivot]
    middle = [x for x in  arr if x==pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return quick_select(left,k)
    elif k< len(left)+len(middle):
        return pivot
    else:
        return quick_select(right,k-len(left)-len(middle))