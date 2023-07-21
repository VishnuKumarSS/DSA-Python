# Data Structures & Algorithms - Notes

Created: June 10, 2023 5:02 PM
Updated: July 21, 2023 9:51 PM

# Linked List:

**Time Complexities:**

Append to the end of linked list: O(1)

Removing at the end of linked list: O(n)

Append at the beginning of the linked list: O(1)

Removing at the beginning of the linked list: O(1)

Append to the middle of the linked list: O(n)

Remving at the middle of the linked list: O(n)

Lookup with the value: O(n) 

Lookup with the index: O(n), **but with the normal list it’s O(1)**

**Linked List vs List Time Complexity:**

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled.png)

---

# **GRAPHS**

**ADJACENT MATRIX:**

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%201.png)

Here the yellow A,B,C,D,E are the actual vertices and the grey A,B,C,D,E are the edges.

when It’s bidirectional Adjacency matrix, It will have the 45 degree line of zeroes.

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%202.png)

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%203.png)

But when these are directional, then it will be like that

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%204.png)

And if the edges are weighted, then we should put the numbers instead of 1’s.

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%205.png)

---

**ADJACENCY LIST:**

We will represent it with dictionaries.

We should mention the vertices a particular vertex points to, by

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%206.png)

The overall representation of the adjacency list is

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%207.png)

---

**GRAPH’s BIG O:**

Adjacency matrix vs Adjacency list,

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%208.png)

Adding just a new vertex without edges, time complexity:

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%209.png)

Adding just the **edges** with **existing** vertices, time complexity:

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2010.png)

The resulting graph will look like this,

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2011.png)

---

Removing a edge between vertices time complexity:

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2012.png)

Removing a vertex time complexity,

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2013.png)

---

At the end, Adjacenty List (**better**) is more time and space efficient than Adjacenty Matrix.

---

# **RECURSION:**

Recursion in python is a function that calls itself until a base case is reached. The base case is where the function stops calling itself, without which a Stack Overflow error will occur. Recursion consists of two cases: the base case and the recursive case. The base case is where the function stops calling itself, and the recursive case is where the function continues to call itself. A common example of recursion in Python is calculating the factorial of a number.

A function that calls itself, until it doesn’t.

**Two cases:**

1. **Base case** - Where the function stops calling itself (Without this, **Stack Overflow** will occur)
2. **Recursive case** - When the function call continues calling itself

**Example:**

Factorial of 4 (i.e) **4!** is 4 * 3 * 2 * 1

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))
```

![Code flow explanation.](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2014.png)

Code flow explanation.

![Explanation with Call stack.](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2015.png)

Explanation with Call stack.

---

# Sorting algorithms:

**Bubble Sort:**

**Bubble sort is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted and comparing adjacent elements and swapping them if they are in the wrong order. The pass through the list is repeated until the list is sorted.**

Here is the algorithm for bubble sort:

1. Start at the beginning of the list
2. Compare the first two elements. If the first is greater than the second, swap them.
3. Compare the second and third elements. If the second is greater than the third, swap them.
4. Continue comparing adjacent elements and swapping them until the end of the list is reached.
5. Repeat the steps for the entire list until no more swaps are needed.

Bubble sort has a worst-case and average complexity of O(n^2), where n is the number of items being sorted. However, it has the advantage of being easy to understand and implement.

**Selection Sort:**

**In selection sort we will have a minimum_index in each iteration, and compare it with all the elements. If other element is less than the minimum_index element, then that element’s index is the min index. When we reach the end of the list, we will swap the elements with the current i th element.**

Below is the first iteration, means the **min_index** at the start is 0. Here we will swap the index 4 th element with index 0 th element

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2016.png)

I haven’t pasted the picture for second iteration as that is already sorted. 

Below is the third iteration means the **min_index** at the start is **2.** Here we will swap the index 5 th element with the index 2 nd element

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2017.png)

Selection sort has a worst-case and average complexity of O(n^2), where n is the number of items being sorted. It is an in-place comparison sort and can be unstable.

**Insertion Sort:**

**In insertion sort we always start with the second item in the list, and then we compare it to the previous items, if it’s less than the item before it we will swap those items until the item is not less than the previous item.**

It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

- Simple implementation
- Efficient for (quite) small data sets, much like other quadratic sorting algorithms
- More efficient in practice than most other simple quadratic (i.e., O(n^2)) algorithms such as selection sort or bubble sort

Insertion sort has a worst-case and average complexity of O(n^2), where n is the number of items being sorted.

---

## **Merge Sort:**

Merge sort is a divide-and-conquer algorithm that works by splitting an array or list into smaller subarrays, sorting those subarrays, and then merging them back together. It is a stable, comparison-based algorithm that has a worst-case and average complexity of O(n log n), where n is the number of items being sorted.

The basic algorithm for merge sort is as follows:

1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

Merge sort is known for its efficiency, especially when sorting large amounts of data. It is also a popular choice for sorting linked lists, as it performs well on this data structure due to its efficient use of memory.

**Merge Sort procedure we can follow:**

![Untitled](Data%20Structures%20&%20Algorithms%20-%20Notes%200ff0acd108914818a8d1a36cf0fe0a17/Untitled%2018.png)

---
