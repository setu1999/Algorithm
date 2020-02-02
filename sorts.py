#insertion sort
def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 

#bubble sort


def bubbleSort(arr):
	n = len(arr)

	for i in range(n):

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64,89,90,89,67,56,45,78]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])
#counting sort

def countSort(arr): 

	output = [0 for i in range(256)] 


	count = [0 for i in range(256)] 

	ans = ["" for _ in arr] 

	for i in arr: 
		count[ord(i)] += 1

	for i in range(256): 
		count[i] += count[i-1] 

	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1

	
	for i in range(len(arr)): 
		ans[i] = output[i] 
	return ans 
 
arr = "geeksforgeeks"
ans = countSort(arr) 
print "Sorted character array is %s" %("".join(ans)) 
#selection sort

import sys 
A = [64, 25, 12, 22, 11] 

for i in range(len(A)): 
	
	
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
		 
	A[i], A[min_idx] = A[min_idx], A[i] 

print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i]), 
#merge sort

def merge(arr, l, m, r): 
	n1 = m - l + 1
	n2 = r- m 

	L = [0] * (n1) 
	R = [0] * (n2) 

		for i in range(0 , n1): 
		L[i] = arr[l + i] 

	for j in range(0 , n2): 
		R[j] = arr[m + 1 + j] 


	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			arr[k] = L[i] 
			i += 1
		else: 
			arr[k] = R[j] 
			j += 1
		k += 1

	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1
	while j < n2: 
		arr[k] = R[j] 
		j += 1
		k += 1
def mergeSort(arr,l,r): 
	if l < r: 

		# Same as (l+r)/2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))/2

		# Sort first and second halves 
		mergeSort(arr, l, m) 
		mergeSort(arr, m+1, r) 
		merge(arr, l, m, r) 


# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
	print ("%d" %arr[i]), 

mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
	print ("%d" %arr[i]), 
 

