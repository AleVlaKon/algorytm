def count_triplet_numbers(data):
	max_value = max(data)


	counts = [0] * (max_value + 1)
	
	#заполняем вспомогательный список значениями
	for element in data:
		counts[element] += 1
		
	index = 0

	for num in counts:
		if num == 3:
			index += 1
			
	return index


print(count_triplet_numbers([4, 5, 6, 4, 5, 4, 5, 6]))
print(count_triplet_numbers([5, 4, 5, 5, 4, 5, 7, 4]))
print(count_triplet_numbers([4, 5, 4, 6, 5, 7, 5, 5]))
print(count_triplet_numbers([7, 7, 7]))   