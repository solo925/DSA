# recursin

# time complexity O(n)
# space complexity O(n)

# def recursive(n):
#     if n <= 1:
#         return n
#     return n + recursive(n - 1)

# print(recursive(5))

# recursive jump
# Time complexity O(n)
#space complexity O(n)
def jump(n,acc=0):
    if n <= 1:
        return acc
    return (jump(n-1,acc+n))
    
