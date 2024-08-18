

def mergeKLists(lists):
    class MinHeap:
        def __init__(self):
            self.heap = []

        def size(self):
            return len(self.heap)

        def _heapify_up(self, index):
            parent = (index - 1) // 2
            if index > 0 and self.heap[index].val < self.heap[parent].val:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self._heapify_up(parent)

        def _heapify_down(self, index):
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < self.size() and self.heap[left_child].val < self.heap[smallest].val:
                smallest = left_child
            if right_child < self.size() and self.heap[right_child].val < self.heap[smallest].val:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                self._heapify_down(smallest)

        def push(self, node):
            self.heap.append(node)
            self._heapify_up(self.size() - 1)

        def pop(self):
            if self.size() == 0:
                return None
            smallest = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(0)
            return smallest


    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    # Initialize a custom min-heap
    min_heap = MinHeap()

    # Push the first node of each list into the heap
    for l in lists:
        if l:
            min_heap.push(l)

    # Dummy head for the result linked list
    dummy = ListNode()
    current = dummy

    # While there are nodes left in the heap
    while min_heap.size() > 0:
        # Extract the smallest node
        smallest_node = min_heap.pop()
        # Add the smallest node to the result
        current.next = smallest_node
        current = current.next

        # If there's a next node in the list, push it to the heap
        if smallest_node.next:
            min_heap.push(smallest_node.next)

    # Return the merged linked list
    return dummy.next




    
