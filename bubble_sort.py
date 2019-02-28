def bubble_sort(array):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				swapped = True
	return array




test_array = [5, 1, 4, 2, 8]
print(bubble_sort(test_array))