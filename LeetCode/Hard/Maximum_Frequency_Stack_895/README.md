
# FreqStack Class

## Description
The `FreqStack` class implements a frequency stack that allows for the pushing and popping of integers based on their frequency of occurrence within the stack. The element with the highest frequency is the one that is popped from the stack. If multiple elements have the same maximum frequency, the most recently added element is popped.

## Implementation Details
- `FreqStack` uses two main data structures:
  - `val_freq_map`: A dictionary that maps values to their current frequencies in the stack.
  - `freq_nodes_map`: A dictionary that maps frequencies to a doubly-linked list of nodes (elements with the same frequency).
- The class includes a nested `Node` class for the doubly-linked list implementation.

## Detailed Algorithm
1. **Initialization**:
   - The `FreqStack` is initialized with no elements, setting `maxfreq` to 0 and initializing two dictionaries: `val_freq_map` and `freq_nodes_map`.

2. **Push Operation**:
   - Check if the value exists in `val_freq_map`:
     - If yes, increment its frequency.
     - If no, set its frequency to 1 and add to `val_freq_map`.
   - Create a new node with the value.
   - If this frequency is seen for the first time, initialize with this node.
   - If this frequency has been seen before, append the new node to the right of the last node at this frequency and update links.
   - Update `maxfreq` if the current frequency of the value is the new maximum.

3. **Pop Operation**:
   - Find the node with the highest frequency (`maxfreq`).
   - Update the frequency of the node’s value in `val_freq_map`, decrease by 1, or remove if frequency becomes zero.
   - Adjust the doubly linked list:
     - If node has a left neighbor, remove the node by updating links.
     - If it's the only node at this frequency, update `freq_nodes_map`.
   - Recalculate `maxfreq` if necessary.
   - Return the value of the popped node.

## Usage
To use this stack, instantiate an object of the `FreqStack` class, and then use the `push` and `pop` methods to add and remove elements, respectively.

### Example
```python
obj = FreqStack()
obj.push(10)
obj.push(20)
obj.push(10)
result = obj.pop()  # Returns 10, as it is the most frequent
```

Feel free to extend or modify the implementation to fit specific requirements.
