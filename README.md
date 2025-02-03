# Sorting Algorithms Repository 🚀

Welcome to the **Sorting Algorithms Repository**! 🎉  
This repository contains implementations of three fundamental sorting algorithms in Python: **Bubble Sort**, **Insertion Sort**, and **Selection Sort**. Whether you're a beginner learning about algorithms or an experienced programmer brushing up on the basics, this repository is for you! 💻

---

## Table of Contents 📚
1. [Bubble Sort](#bubble-sort)
2. [Insertion Sort](#insertion-sort)
3. [Selection Sort](#selection-sort)
4. [How to Use](#how-to-use)
5. [Contribution](#contribution)
6. [License](#license)

---

## 1. Bubble Sort 🛁

 ### Description:
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

 ### Time Complexity:
- **Best Case**: O(n) - When the list is already sorted.
- **Average Case**: O(n²) - When the list is randomly ordered.
- **Worst Case**: O(n²) - When the list is sorted in reverse order.

### Space Complexity:
- O(1) - Bubble Sort is an **in-place sorting algorithm** and requires no additional memory.

### Code Example:
```
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr
```

---

## 2. Insertion Sort 📥

### Description:
Insertion Sort builds the final sorted array one element at a time. It iterates through the list and inserts each element into its correct position in the sorted portion of the array.

### Time Complexity:
**Best Case:** O(n) - When the list is already sorted.

**Average Case:** O(n²) - When the list is randomly ordered.

**Worst Case:** O(n²) - When the list is sorted in reverse order.

### Space Complexity:
O(1) - Insertion Sort is an in-place sorting algorithm and requires no additional memory.

### Code Example:
```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr
```
---

## 3. Selection Sort 🎯

### Description:
Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first unsorted element. This process continues until the entire list is sorted.

### Time Complexity:
**Best Case:** O(n²) - Even if the list is already sorted, the algorithm still performs comparisons.

**Average Case:** O(n²) - When the list is randomly ordered.

**Worst Case:** O(n²) - When the list is sorted in reverse order.

### Space Complexity:
O(1) - Selection Sort is an in-place sorting algorithm and requires no additional memory.

### Code Example:

```
def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr
```
---

## 4. How to Use 🛠️

**1.Clone the repository:**
```
git clone https://github.com/Sunilyadav03/Sorting_Techniques.git
```
**2.Navigate to the repository:**
```
cd Sorting_Techniques
```
**3.Run the Python scripts to see the sorting algorithms in action:**
```
python Bubble_Sort.py
python Insertion_sort.py
python selection_sort.py
```
---

## 4. Contribution 🤝
Contributions are welcome! 🎉 If you have suggestions for improvements or additional sorting algorithms, feel free to:

  Open an issue.
  
  Submit a pull request.

Let's make this repository even better together! 💪

## 5. License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

