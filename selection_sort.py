## SELECTION SORT

#Selection Sort is a comparison-based sorting algorithm.
#Does not maintain the relative order of equal elements which means it is not stable.
#Selection Sort is an in-place sorting algorithm and requires only O(1) additional space.
# Selection Sort selects the minimum element and places it in the correct position with fewer swaps, while Bubble Sort repeatedly swaps adjacent elements to sort the array.

def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(selection_sort(arr))