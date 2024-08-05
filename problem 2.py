list = list(map(int, input("Enter the list of numbers: ").split()))
n = int(input("Enter the amount of numbers in the list "))
def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    real_sum = sum(numbers)
    missing_num = expected_sum - real_sum
    return missing_num
result = missing_number(list, n)
print(f"The missing number is {result}")