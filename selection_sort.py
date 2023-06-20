def find_min_index(arr):
	min_index = 0

	for index in range(1, len(arr)):
		if arr[index] < arr[min_index]:
			min_index = index

	return min_index

def selection_sort(arr):
	sorted_arr = []

	for element in range(len(arr)):
		min_index = find_min_index(arr)

		sorted_arr.append(arr.pop(min_index))

	return sorted_arr


print(selection_sort([38, 10, 39, 50, 51, 59, 15, 9, 25]))
