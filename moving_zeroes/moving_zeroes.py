'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    run = True
    count_zero = 0
    while run:
        for i, v in enumerate(arr):
            if v == 0:
                arr.insert(len(arr), v)
                arr.pop(i)
                count_zero += 1

        if count_zero == len(arr):
            return arr

        if arr[0] == 0:
            run = True

        else:
            run = False

    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 0]
    # [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")