'''
Input: an integer
Returns: an integer
'''
# from itertools import product

# def eating_cookies(n):
#     # Your code here
#     total = 0
#     checker = 0
#     run = True
#     iterator = 1
#     while run:
#         total_checker = 0
#         comb = product([1,2,3], repeat = iterator)
#         for i in comb:
#             if sum(i) == n:
#                 total += 1
#                 total_checker += 1
#                 if checker == 0:
#                     checker = iterator
        
#         if total_checker == 0 and checker > 0:
#             print(iterator)
#             run = False

#         iterator += 1
        

#     return total


def eating_cookies(n):
    if n == 0:
        return 1
    elif n == -1:
        return 0
    elif n == -2:
        return 0
    eat1 = eating_cookies(n-1)
    eat2 = eating_cookies(n-2)
    eat3 = eating_cookies(n-3) 
    
    return eat1 + eat2 + eat3

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
