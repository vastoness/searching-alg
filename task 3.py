def number_of_occurrences():
    nums= list(map(int, input("Enter a list of numbers : ").split()))
    occurrences = {}

    for i in range(len(nums)):
        num = nums[i]
        if num in occurrences:
            occurrences[num]['count'] += 1
            occurrences[num]['last_index'] = i
        else:
            occurrences[num] = {'count': 1, 'first_index': i, 'last_index': i}

    for num, data in occurrences.items():
        if data['count'] > 1:
            print(f"The number {num} occurs {data['count']} times.")
            print(f" first {num} ")
            print(f" last {num}")

number_of_occurrences()
