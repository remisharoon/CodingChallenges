# Mountain Array Search Algorithm

## Description
This Python module contains the implementation of a search algorithm designed to find a specific target value within a 'mountain array'. A mountain array is defined as an array that increases to a peak value and then decreases. The implementation makes use of a binary search algorithm to efficiently locate the target value in both the increasing and decreasing segments of the mountain array.

## Components

- `MountainArray`: An interface for the mountain array. It includes:
  - `get(index: int) -> int`: Method to get the element at a given index.
  - `length() -> int`: Method to get the length of the array.

- `Solution`: A class that contains the method `findInMountainArray` to locate the target value in the mountain array.

### Method: findInMountainArray
- **Parameters**:
  - `target (int)`: The target value to find in the mountain array.
  - `mountain_arr (MountainArray)`: The mountain array object.
- **Returns**:
  - `int`: The index of the target value in the mountain array. Returns -1 if the target is not found.

### Strategy
1. **Peak Finding**: First, identify the peak of the mountain array using a modified binary search.
2. **Binary Search**:
   - Perform a binary search on the ascending part of the array up to the peak.
   - Perform a binary search on the descending part from the peak to the end of the array.
3. **Caching**: To minimize the number of calls to `get`, a caching mechanism is implemented.

## Usage
Instantiate a `MountainArray` and use the `findInMountainArray` method of the `Solution` class to find the index of the target value.

## Example
```python
mountain_array = MountainArrayImplementation()  # Assume some implementation of MountainArray
solution = Solution()
index = solution.findInMountainArray(10, mountain_array)
print("Index of target is:", index)
```

## Note
This implementation assumes the existence of the `MountainArray` class/interface with the necessary methods implemented as described.
