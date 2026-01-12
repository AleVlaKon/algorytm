def counting_sort(data):
	max_value = max(data)

	# делаем вспомогательный список
	counts = [0] * (max_value + 1)
	
	#заполняем вспомогательный список значениями
	for element in data:
		counts[element] += 1
		
	index = 0

	for num in range(max_value + 1):
		for _ in range(counts[num]):
			data[index ] = num
			index += 1

data = [3, 0, 3, 4, 6, 3, 1, 1, 3, 6, 3, 1, 1, 4]
counting_sort(data)

