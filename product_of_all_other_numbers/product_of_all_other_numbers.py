'''
Input: a List of integers
Returns: a List of integers
'''
import numpy
def product_of_all_other_numbers(arr):
    # Your code here
    new_arr = []
    for i, _ in enumerate(arr):
        if i == 0:
            lst2 = arr[i+1:]
            new_arr.append(numpy.prod(lst2))
        else:
            lst1 = arr[:i]
            lst2 = arr[i+1:]
            lst3 = lst1 + lst2
            new_arr.append(numpy.prod(lst3))

    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
