def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		value = array[i]
		hole = i
		while ((hole > 0) and (array[hole-1]>value)):
			array[hole] = array[hole - 1]
			hole -= 1
		array[hole] = value


test_array = [3,4,1,8,7,5,6,2]
print(test_array)
insertion_sort(test_array)
print(test_array)

