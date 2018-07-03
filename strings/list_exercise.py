# numbers = [-1,-2,4,7,10,15,]

# def sum_of_numbers(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print sum_of_numbers(numbers)

# def largest_number(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# print largest_number(numbers)

# def smallest_number(nums):
#     smallest = nums[0]
#     for num in nums:
#         if num < smallest:
#             smallest = num
#     return smallest

# print smallest_number(numbers)

# def even_numbers(nums):
#     even = []
#     for num in nums:
#         if num % 2 == 0:
#             even.append(num)
#     return even
# print even_numbers(numbers)  

# def positive_numbers(nums):
#     positive = []
#     for num in nums:
#         if num > 0:
#             positive.append(num)
#     return positive

# print positive_numbers(numbers)


# def multiply_a_list(nums, factor):
#     multiplied = []
#     for num in nums:
#         product = num * factor
#         multiplied.append(product)
#     return multiplied

# print multiply_a_list(numbers, factor)

# vector1 = [4,-7,-10,5]
# vector2 = [2,3,-3,-5]

# def multiply_vectors(v1,v2):
#     multiplied = []
#     for i in range(len(vector1)):
#         product = v1[i] * v2[i]
#         multiplied.append(product)
#     return multiplied
        
# print multiply_vectors(vector1, vector2)

# matrix1 = [[2, -2], [5,3]]
# matrix2 = [[5,2], [1,0]]


# def matrix_addition(m1,m2):
#     height = len(m1)
#     width = len(m1[0])
#     result = []
    
#     for i in range(0, height):  
#         result.append([])
#         for j in range(0, width):
#             result[i].append(0)

#     for i in range(0, height):
#         for j in range(0, width):
#             cell1 = m1[i][j]
#             cell2 = m2[i][j]

#             result[i][j] = cell1 + cell2
    
#     return result

# print matrix_addition(matrix1, matrix2)

# things = ['apple', 'cheese', 'milk', 'cheese', 'bread', 'cheese']

# def dedup(words):
#     deduped = []
#     for word in words:
#         if word not in deduped:
#             deduped.append(word)
#     return deduped

# print dedup(things) 




# matrix1 = [ [1, 2, 3],
#     [3,4, 5], [2, 122, 344]]
# matrix2 = [[5, 6, 2],
#     [7, 8, 3], [1, 2, 677] ]


# # def matrix_add(mat1, mat2):
# #     matrix_total = []
# #     height = len(mat1)
# #     width = len(mat1[0])
# #     for i in range(height):
# #         matrix_total.append([])
# #         for j in range(width):
# #             total = mat1[i][j] + mat2[i][j]
# #             matrix_total[i].append(total)
# #     print matrix_total
# #     return matrix_total
    
# # matrix_add(matrix1, matrix2)


