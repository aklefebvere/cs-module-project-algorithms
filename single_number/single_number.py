'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    for i in arr:
        dupe = 0
        for v in arr:
            if i == v:
                dupe += 1
                if dupe > 1:
                    break
        if dupe == 1:
            return i
               
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")