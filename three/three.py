def sort(array):
   for i in range(len(array)):
        if (i % 2 == 1) == (array[i - 1] > array[i]):
            array[i], array[i-1] = array[i-1], array[i]
            
 
array = list(map(int, input().split())) 
sort(array)
print(array)