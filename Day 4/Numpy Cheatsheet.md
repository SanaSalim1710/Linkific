# Numpy Cheatsheet with Examples

## Importing
```import numpy as np```   
```
Importing numpy
```
```np.loadtxt('file.txt')```
```
Importing a text file
```
```np.load("file.npy")```
```
Loading a file
```


## Array Creation
```np.array()```
```
Creates array

1D array: arr = np.array([1, 2, 3])
[1 2 3]

2D array: arr = np.array([(1, 2, 3), (4, 5, 6)])
[[1 2 3]
 [4 5 6]]
```
```arr = np.zeros(3)```
```
Creates 1D array of length 3. Every element of the array is 0.

 [0. 0. 0.]
```
```arr = np.ones((3,2))```
```
Creates a new array of given shape and type. Each element is 1

[[1. 1.]
 [1. 1.]
 [1. 1.]]
```
```np.eye(3)```
```
Creates a 3 by 3 identity matrix

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```
```np.linspace(0, 10, 5)```
```
Array containing 5 values from 0 to 10 that have been evenly divided

[ 0.   2.5  5.   7.5 10. ]
```
```np.arange(0, 21, 4)```
```
Creates an array of values from 0 to 21 (not included) with step 4

[ 0  4  8 12 16 20]
```
```np.full((3, 2), 5)```
```
Creates a 3x2 array where every element is 5

[[5 5]
 [5 5]
 [5 5]]
```
```np.random.rand(4, 5)```
```
Creates a 1x2 array of random float point numbers between 0 and 1. The values change every time it runs.

[[0.13640746 0.36981418]]
```
```np.random.randint(10, size=(2, 3))```
```
Creates a 2x3 array with random integers between 0 and 9

[[8 8 3]
 [9 3 5]]
```

## Properties 

**np.array([(1, 2, 3), (4, 5, 6)])**

```array.size```
```
Returns number of elements in the array

6
```
```array.shape```
```
Returns the dimensions of the array (rows, columns)

(2, 3)
```
```array.dtype```
```
Returns the type of elements in the array

int64
```

## Array Manipulation

array = np.array([1, 2, 3])
2darray = np.array([(1, 2, 3), (4, 5, 6)])

```np.append(array, values)```
```
Appends values to end of array

array2 = np.append(array, [4, 5, 6])
array2
[1 2 3 4 5 6]
```
```np.insert(array, 2, values)```
```
Inserts values into the array before index 2

np.insert(array, 2, 9)
array([1, 2, 9, 3])
```
```np.delete(array, 3, axis=0)```
```
Deletes row on index 3 of arr

np.delete(array,1)
array([1, 3])

np.delete(2darray,1,0)
[[1 2 3]]
```
```np.delete(array, 4, axis=1)```
```
Removes the 5th column from array

np.delete(2darray,1,1)
[[1 3]
 [4 6]]
```

```arr.reshape(2, 3)```
```
Reshapes the array to 2 rows and 3 columns without changing contents of array
```

```arr.resize((2, 3))```
```
Changes shape of array to 2x3 and fills new values with 0
```

```np.concatenate((array1, array2), axis=0)```
```
Adds array 2 as rows to end of array 1
```

```np.concatenate((array1, array2), axis=1)```
```
Adds array 2 as columns to end of array 1
```

## Sorting 
```array.sort()```
```
Sorts array

a = np.array([3,1,2])
a.sort()
print(a)
[1 2 3]

## Math
```
```np.mean(arr, axis=0)```
```
Returns mean along specified axis
```
```arr.sum()```
```
Returns sum of elements in array
```
```arr.min()```
```
Returns element with lowest value in array
```
```arr.max()```
```
Returns element with highest value in array
```
```np.std(arr, axis=1)```
```
Returns standard deviation of elements along specified axis in array
```
```np.var(arr)```
```
Returns variance of elements in array
```
```np.add(2)```
```
Adds 2 to each array element
```
```np.subtract(2)```
```
Subtracts 2 from each array element
```
```np.multiply(2)```
```
Multiplies each array element by 2
```
```np.add(2)```
```
Divides each array element by 2 (returns np.nan for division by zero)
```
```np.power(2)```
```
Raise each array element to power of 5
```