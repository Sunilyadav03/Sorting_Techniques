# BUBBLE SORT
          
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity are quite high.
# It does not require any additional memory space.
# It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.   
# Bubble sort has almost no or limited real world applications. It is mostly used in academics to teach different ways of sorting.
# Bubble sort takes minimum time (Order of n) when elements are already sorted. Hence it is best to check if the array is already sorted or not beforehand, to avoid O(n2) time complexity.
# it is an in-place algorithm.
# the bubble sort algorithm is stable.

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr




# 

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(bubble_sort(arr))
    
    
