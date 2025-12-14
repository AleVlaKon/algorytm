def count_beautiful_pairs(nums):
	max_value = max(nums)
	counts = [0] * (max_value + 1)

	for element in nums:
		counts[element] += 1
	res = 0
	for i in counts:
		res += i // 2

	return res