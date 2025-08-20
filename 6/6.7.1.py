def matrix_search(matrix: list, target: int):
    for line in matrix:
        left, right = 0, len(line) - 1    
        
        while left <= right:
            middle = (left + right) // 2  
            elem = line[middle]         
            
            if elem == target:            
                return True               
            
            if elem < target:              
                left = middle + 1           
            else:                           
                right = middle - 1          
        
    return False


data = [[-21, 2, 7, 8, 17], 
        [-9, -2, -1, 4, 9], 
        [-18, -11, -7, -6, 23], 
        [-17, 0, 10, 18, 22], 
        [-24, -15, -10, 11, 16]]
        
print(matrix_search(data, 16))