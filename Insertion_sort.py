# INSERTION SORT

# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.
# We start with second element of the array as first element in the array is assumed to be sorted.
# Compare second element with the first element and check if the second element is smaller then swap them.
# Move to the third element and compare it with the first two elements and put at its correct position
# Repeat until the entire array is sorted.

# When is the Insertion Sort algorithm used?---->Insertion sort is used when number of elements is small. It can also be useful when the input array is almost sorted, and only a few elements are misplaced in a complete big array. 
# What is the Algorithmic Paradigm of the Insertion Sort algorithm?--->The Insertion Sort algorithm follows an incremental approach. 
# What are the Boundary Cases of the Insertion Sort algorithm?--->Insertion sort takes the maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted. 
# Insertion sort is a in-place and stable sorting algorithm.
# Can be useful when array is already almost sorted (very few inversions)
# Since Insertion sort is suitable for small sized arrays, it is used in Hybrid Sorting algorithms along with other efficient algorithms like Quick Sort and Merge Sort.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(insertion_sort(arr))