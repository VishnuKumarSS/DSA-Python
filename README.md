# Data Structures & Algorithms - Notes (Python)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6870d587-ea47-41d6-a2f3-64344f9fd384/Untitled.png)

---

# **GRAPHS**

**ADJACENT MATRIX:**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c8a6b15-3045-4b1a-baac-1365faf22c03/Untitled.png)

Here the yellow A,B,C,D,E are the actual vertices and the grey A,B,C,D,E are the edges.

when It’s bidirectional Adjacency matrix, It will have the 45 degree line of zeroes.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9949b814-24f3-4442-9e5c-ab3268ecf126/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76bc69f3-8546-4cdb-941f-a33b29db1df8/Untitled.png)

But when these are directional, then it will be like that

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14cf85ab-d8c5-438c-a12b-4199fa096cae/Untitled.png)

And if the edges are weighted, then we should put the numbers instead of 1’s.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f486dd11-2f1a-43ad-ba71-12957450efe8/Untitled.png)

---

**ADJACENCY LIST:**

We will represent it with dictionaries.

We should mention the vertices a particular vertex points to, by

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/baf7fd36-2a72-43c4-81fe-ef503b63fcca/Untitled.png)

The overall representation of the adjacency list is

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a6b7df1-8afe-4599-95c5-96011578d226/Untitled.png)

---

**GRAPH’s BIG O:**

Adjacency matrix vs Adjacency list,

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a90a465e-d701-4867-9388-4618034c836c/Untitled.png)

Adding just a new vertex without edges, time complexity:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/23c9c1c0-abb7-4214-9457-5afab405e0b1/Untitled.png)

Adding just the **edges** with **existing** vertices, time complexity:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7ec365e-3615-4480-8dc6-5e137e3ddc7c/Untitled.png)

The resulting graph will look like this,

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6bc29038-93d7-4da4-8856-ed1c23a58bb9/Untitled.png)

---

Removing a edge between vertices time complexity:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e34c7342-d771-40bb-9765-7bb9cfac28cd/Untitled.png)

Removing a vertex time complexity,

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0a2e2b9-31ec-4e85-b92d-21f9f923f8bf/Untitled.png)

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

![Code flow explanation.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/187e309a-f0ce-4f49-9e61-3633409a0f2d/Untitled.png)

Code flow explanation.

![Explanation with Call stack.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c40fdf4-2e69-4dba-889f-4182be5506f1/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17b06c88-a98a-4fc8-bcbd-bbd0fd564b62/Untitled.png)

I haven’t pasted the picture for second iteration as that is already sorted. 

Below is the third iteration means the **min_index** at the start is **2.** Here we will swap the index 5 th element with the index 2 nd element

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b65d46ec-3be3-4d51-967e-23e971366cd7/Untitled.png)

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
