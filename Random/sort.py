# Implimentation of various sorting algorithms for lists
##########################

def selection_sort(unsortedList):
	"""
	Look through the list.  Find the smallest element.  Swap it to the front.
	Repeat.
	"""
	for inx, element in enumerate(unsortedList):
		smallest = unsortedList[inx]
		position = inx
		for count in range(inx, len(unsortedList)):
			if smallest > unsortedList[count]:
				smallest = unsortedList[count]
				position = count
		if position != inx:
			transitory = unsortedList[inx]
			unsortedList[inx] = unsortedList[position]
			unsortedList[position] = transitory
	return unsortedList

def insertion_sort(unsortedList):
	"""
	Insert (via swaps) the next element in the sorted list of the previous
	elements.
	"""
	for inx in range(1, len(unsortedList)):
		if unsortedList[inx] < unsortedList[inx - 1]:
			for count in range (inx, 0, -1):
				if unsortedList[count] < unsortedList[count - 1]:
					transitory = unsortedList[count - 1]
					unsortedList[count - 1] = unsortedList[count]
					unsortedList[count] = transitory
				else:
					break
	return unsortedList

def merge_sort(firstListFragment, secondListFragment = []):
	"""
	Our first recursive algorithm.
	"""
	length = len(firstListFragment)
	if length > 1:
		firstListFragment = merge_sort(firstListFragment[:length//2], firstListFragment[length//2:])	
	length = len(secondListFragment)
	if length > 1:
		secondListFragment = merge_sort(secondListFragment[:length//2], secondListFragment[length//2:])
	return merge(firstListFragment, secondListFragment)

def merge(firstListFragment, secondListFragment):
	"""
	merge the two lists
	"""
	left = 0
	right = 0
	leftLength = len(firstListFragment)
	rightLength = len(secondListFragment)
	result =[]
	while left < leftLength and right < rightLength:
		if firstListFragment[left] <= secondListFragment[right]:
			result.append(firstListFragment[left])
			left += 1
		else:
			result.append(secondListFragment[right])
			right += 1
	result.extend(firstListFragment[left:])
	result.extend(secondListFragment[right:])
	return result