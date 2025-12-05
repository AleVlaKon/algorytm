def insertion_sort(data):
	n = len(data)
	
	for i in range(1, n):
		item = data[i]
		j = i - 1
		
		while j >= 0 and item > data[j]: 
			data[j + 1] = data[j]        
			j -= 1                     
			
			
		data[j + 1] = item 