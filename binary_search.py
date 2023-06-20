def binary_search(arr, item): 
	start = 0;
	end = len(arr) - 1;

	while start <= end:
		mid = (start + end) // 2

		if(arr[mid] == item):
			return mid

		if item > arr[mid]:
			start = mid + 1

		if item < arr[mid]:
			end = mid - 1
	
	return -1
	
