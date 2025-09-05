
# first approach
# Time = O(n²)
# Space = O(n)
def findTheWinner(n, k):
    arr = [i+1 for i in range(n)]
    
    def helper(arr, start_index):
        if len(arr) == 1:
            return arr[0]
        remove = (start_index + k - 1) % len(arr)
        del arr[remove]
        return helper(arr, remove)
    
    return helper(arr, 0) 


# method 2
# Time: O(n) (one recursion per friend)
# Space: O(n) (recursion stack)

def findTheWinner(n, k):
    
    def josephus(n, k):
        if n == 1:
            return 0
        else:
            return (josephus(n - 1, k) + k) % n
    return josephus(n,k) + 1
# Itterative approach
# Time: O(n)
# Space: O(1)
def findTheWinner(n, k):
    result = 0
    for i in range(1, n + 1):
        result = (result + k) % i
    return result + 1