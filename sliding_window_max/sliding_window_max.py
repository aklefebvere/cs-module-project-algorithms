'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    slide = []
    max_slide = []
    for i in range(k):
        slide.append(nums[i])
    
    for i in nums[k:]:
        max_slide.append(max(slide))
        slide.pop(0)
        slide.append(i)

    max_slide.append(max(slide))

    return max_slide


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
