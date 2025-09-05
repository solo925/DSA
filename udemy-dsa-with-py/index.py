# import array


# def sorted_squares(array)->array:
#     if not hasattr(array,"__iter__") or isinstance(array,(str,bytes)):
#         raise TypeError("input must be an iterable of numbers (not stwring or bytes)")
#     result = []
    
#     for x in array:
#         if not isinstance(x,(float,int)):
#             raise ValueError(f"All elemnet must be numbers.Found: {x} of type {type(x)}")
#         result.append(x**2)
#     return sorted(result)

# print(sorted_squares([1,3,4,5,6,7,88,]))
# print(sorted_squares([]))
# print(sorted_squares([1,"b",4,6]))

my_array = [-7, 1, 5, 2, -4, 3, 0]
for i,value in enumerate(my_array):
    print(f"{i}:{value}")
    
    
    print(len(my_array))
# def find_equilibrium(array:list[int])->int:
#     # initial values
#     total_sum = sum(array)
#     left_sum = 0
    
#     for i,value in enumerate(array):
#         total_sum-=value
#         if total_sum == left_sum:
            
        
    



