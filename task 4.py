def rotated_sorted_array():
    nums = list(map(int, input("Enter a sorted list  ").split()))
    l,r = 0, len(nums) - 1
    rotation = 0

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    rotation = l
    print(f" rotations are {rotation}")
rotated_sorted_array()
