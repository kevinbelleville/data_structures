def merge_sort(array):
	length_array = len(array)
	if length_array < 2:
		return 
	mid = length_array//2
	left = []
	right = []
	for i in range(0, mid):
		left.append(array[i])
	for i in range(mid, length_array):
		right.append(array[i])

	merge_sort(left)
	merge_sort(right)

	merge(array, left, right)

	return


	
# define a helper method merge
def merge(array, left, right):
	# take two sorted arrays, left and right, and merge in place into array
	l_index = 0
	r_index = 0
	a_index = 0
	while ((l_index < len(left)) and (r_index < len(right))):
		if left[l_index] < right[r_index]:
			array[a_index] = left[l_index]
			l_index += 1
		else:
			array[a_index] = right[r_index]
			r_index += 1

		a_index += 1

	while (l_index < len(left)):
		array[a_index] = left[l_index]
		l_index += 1
		a_index += 1

	while (r_index < len(right)):
		array[a_index] = right[r_index]
		r_index += 1
		a_index += 1


	return


test_array = [8, 3, 1, 7, 0, 10, 2]
print(test_array)
merge_sort(test_array)
print(test_array)