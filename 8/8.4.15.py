def least_frequent_number(data):
	max_value = max(data)

	counts = [0] * (max_value + 1)
	
	for element in data:
		counts[element] += 1
		
	min_value = max(counts)

	for num in counts:
		if num > 0 and num < min_value:
			min_value = num
			
	return counts.index(min_value)