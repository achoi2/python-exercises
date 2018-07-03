# def fibonacci_sequence(number):
#     num1 = 1
#     num2 = 1
#     total = 0
#     while number <= 40:
#         num3 = num1 + num2
#         if num3 % 2 == 0:
#             total += num3
#         num1 = num2
#         num2 = num3
#     return total

# fibonacci_sequence(40)


# nums = 13195

# factor_list = []

# prime_list = []

# for i in range(2, nums):
#     if nums % i  == 0:
#         factor_list.append(i)
            
# print factor_list

# for factor in factor_list:
#     isprime = True
#     for j in range(2, factor):
#         if factor % j == 0:
#             isprime = False

#     if isprime == True:
#         prime_list.append(factor)
    
        

# print prime_list[-1]   
number = 600851475143

remainder = number
factor = 2
while remainder != 1:
    if remainder % factor == 0:
        remainder /= factor
    else: 
        factor += 1 

print factor

            
#... when the remainder is = 1

        
        


