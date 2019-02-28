# select a pivot (random)
# rearrange the array such that everything less is on the left
# everything greater is on the right

def quick_sort(array, start, end):
	if start >= end:
		return
	else:
		# partition
		partition_index = partition(array, start, end)

		quick_sort(array, start, partition_index-1)
		quick_sort(array, partition_index+1, end)

	
def partition(array, start, end):
	pivot = array[end]
	partition_index = start
	for i in range(start, end):
		if array[i] <= pivot:
			array[i], array[partition_index] = array[partition_index], array[i]
			partition_index += 1
	array[end], array[partition_index] = array[partition_index], array[end]
	return partition_index



test_array = [7, 2, 1, 6, 8, 5, 3, 4]
print(test_array)
quick_sort(test_array, 0, len(test_array)-1)
print(test_array)