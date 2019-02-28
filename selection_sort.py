def selection_sort(array):
	n = len(array)
	for i in range(0, n):
		min_index = i
		for j in range(i+1, n):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]




test_array = [3,4,8,6,1,5,2,7]
print(test_array)
selection_sort(test_array)
print(test_array)
