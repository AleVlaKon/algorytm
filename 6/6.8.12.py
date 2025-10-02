def is_value(values, target):
# вместо левой границы сначала берем длину 
	# последовательности
	n, right = len(values), 1 
	
	# находим правую границу 
	# как минимальное значение удвоенного индекса и длины
	# а левую принимаем как половину от правой границы
	while right < n and values[right] < target:
		right *= 2
	
	# здесь строки можно переставить местами,	
	# так left будет больше (из комментариев)
	right = min(n - 1, right)
	left = right // 2
	
	# основная часть алгоритма	
	while left <= right:
		middle = (left + right) // 2
		elem = values[middle]
		if elem == target:
			return True
		if elem > target:
			left = middle + 1
		else:
			right = middle - 1
	return False

values1 = [4, -3, -10, -17, -24]
print(is_value(values1, -17))        