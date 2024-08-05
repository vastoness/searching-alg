mylist = list(map(int, input("Enter a mylist of nunms ").split()))
def second_largest(mylist):
    if len(mylist) < 2:
        return None
    diff_nums = list(set(mylist))
    if len(diff_nums) < 2:
        return None
    diff_nums.sort(reverse=True)
    return diff_nums[1]
result = second_largest(mylist)
print(f"The 2nd largest num is {result}")

second_largest(mylist)