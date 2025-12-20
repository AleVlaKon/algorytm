def count_beautiful_pairs(nums):
	max_value = max(nums)
	counts = [0] * (max_value + 1)

	for element in nums:
		counts[element] += 1
	res = 0
	for i in counts:
		res += i // 2

	return res

print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0]))
print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4]))    # пары: (4; 4), (4; 4), (4; 4)
print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7]))