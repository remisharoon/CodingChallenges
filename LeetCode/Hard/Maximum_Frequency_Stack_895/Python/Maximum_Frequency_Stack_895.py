class FreqStack:
    class Node:
        val = None
        left = None
        right = None

        def __init__(self, val):
            self.val = val

    def __init__(self):
        self.val_freq_map = {}
        self.freq_nodes_map = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        if val in self.val_freq_map:
            freq = self.val_freq_map[val]
            freq += 1
        else:
            freq = 1
            self.val_freq_map[val] = freq

        node = self.Node(val)
        if freq not in self.freq_nodes_map:
            self.freq_nodes_map[freq] = node
        else:
            self.freq_nodes_map[freq].right = node
            node.left = self.freq_nodes_map[freq]
            self.freq_nodes_map[freq] = node

        self.val_freq_map[val] = freq
        self.maxfreq = max(freq, self.maxfreq)

    def pop(self) -> int:
        if not self.freq_nodes_map:
            return -1
        node = self.freq_nodes_map[self.maxfreq]
        if self.maxfreq > 1:
            self.val_freq_map[node.val] = self.maxfreq - 1
        else:
            del self.val_freq_map[node.val]
        if node.left is None:
            del self.freq_nodes_map[self.maxfreq]
            if self.freq_nodes_map:
                self.maxfreq = max(self.freq_nodes_map.keys())
            else:
                self.maxfreq = 0
        else:
            node.left.right = None
            self.freq_nodes_map[self.maxfreq] = node.left
        return node.val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()