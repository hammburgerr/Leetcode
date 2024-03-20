# How to solve 
##### 1. reshape is not possible
1. make variables
    - number of elements in original matrix
    - 📕 flatten given matrix
    - check the length of flattened matrix
  
2. number of elements in reshaped matrix
    - r x c

3. compare 1-1) and 1-2)
    - if they're not equal, give the original matrix
    - if they're equal, move to #2.

##### 2. reshape is possible
1. 📕 make an initializer list with shape (r, c)
2. put the elements of flattened matrix into the reshaped matrix

# 📕 To memorize
##### 1. flattening: 
    'flattened = [num for sublist in mat for num in sublist]'
structure: [num / for sublist in mat / for num in sublist ]
- for sublist in mat: This part iterates over each sublist in the list mat.
- for num in sublist: This nested loop iterates over each number (num) in the current sublist.
- num for sublist in mat for num in sublist: This is a list comprehension that combines the above two steps. It essentially flattens the list by iterating over each sublist and then over each number in that sublist.


##### 2. Initializer list:
    'list_ = [[0]*3 for _ in range(3)]'
- result: [[0,0,0], [0,0,0], [0,0,0]]
