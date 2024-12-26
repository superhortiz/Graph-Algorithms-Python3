from typing import Any, Iterator, List, Union


class IndexMinPQ:
    """
    A binary heap implementation of an indexed priority queue (min-heap).
    The index is implicit in the position of the element in the priority queue.

    Lists used:
        pq[i]: Gives the index of the key in the keys list that is currently at the
               ith position in the priority queue. (1-based indexing).
               The minimum value is in pq[1].

        qp[i]: Provides the position in the priority queue of the element with index i.
               In other words, qp[i] gives the position of the element with index i in the pq array.
               They have an inverse relationship: qp[pq[i]] = pq[qp[i]] = i

        keys[i]: It holds the priority values (or keys) associated with each element index.

    Methods:
        contains(i: int) -> bool:
            Checks if the priority queue contains the specified index.

        insert(i: int, key: Any) -> None:
            Inserts a new value into the heap at the specified index.

        del_min() -> Any:
            Removes and returns the minimum value from the heap.

        decrease_key(i: int, key: Any) -> None:
            Decreases the key value of the specified index.

    Inner Classes:
        HeapEmptyError(Exception):
            Custom exception to be raised when attempting to access an element from an empty heap.
    """

    class HeapEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element from an empty heap.
        """
        def __init__(self, message: str = "The heap is empty.") -> None:
            self.message = message
            super().__init__(self.message)

    def __init__(self, max_n: int) -> None:
        """
        Initializes an empty binary heap with a given maximum capacity.

        Args:
            max_n (int): Maximum number of elements the priority queue can hold.
        """
        self._keys: list = [None] * (max_n + 1)
        self._pq: list = [None] * (max_n + 1)
        self._qp: list = [-1] * (max_n + 1)
        self._n: int = 0

    def contains(self, i: int) -> bool:
        """
        Checks if the priority queue contains the specified index.

        Args:
            i (int): Index to check for existence in the priority queue.

        Returns:
            bool: True if the index is in the priority queue, False otherwise.
        """
        return self._qp[i] != -1

    def insert(self, i: int, key: Any) -> None:
        """
        Inserts a new value into the heap at the specified index.

        Args:
            i (int): The index at which the key should be inserted.
            key (Any): The value to be inserted into the heap.
        """
        self._n += 1

        # Add the new element at the end of the heap
        self._pq[self._n] = i

        # Keep track of the position of the new value in the priority queue
        self._qp[i] = self._n
        self._keys[i] = key

        # Restore the heap order by swimming up the new element
        self._swim(self._n)

    def del_min(self) -> Any:
        """
        Removes and returns the index of the minimum key from the heap.

        Returns:
            int: The index of the minimum key from the heap.

        Raises:
            IndexMinPQ.HeapEmptyError: If the heap is empty.
        """
        if self._n == 0:
            raise self.HeapEmptyError()

        # The index of the minimum key in the heap
        min_index = self._pq[1]
        
        # Swap the minimum element with the last element
        self._exchange(1, self._n)
        
        # Decrease the size of the heap
        self._n -= 1
        
        # Restore the heap order by sinking down the new root element
        self._sink(1)
        
        # Remove the last element (formerly the minimum) from the heap
        self._keys[self._pq[self._n + 1]] = None
        self._qp[self._pq[self._n + 1]] = -1
        
        return min_index

    def decrease_key(self, i: int, key: Any) -> None:
        """
        Decreases the key value of the specified index.

        Args:
            i (int): The index of the element to decrease the key for.
            key (Any): The new key value.

        Raises:
            ValueError: If the new key is not smaller than the current key.
        """
        if key < self._keys[i]:
            # Update the key at the specified index
            self._keys[i] = key
            
            # Restore the heap order by swimming up the updated element
            self._swim(self._qp[i])

        else:
            raise ValueError("New key must be smaller than the current key.")

    def _swim(self, k: int) -> None:
        """
        Restores the heap order property by swimming up the element at index k.

        Args:
            k (int): The index of the element in the priority queue to swim up.
        """
        while k > 1 and self._greater(k // 2, k):
            # If the parent is greater than the child, exchange them
            self._exchange(k, k // 2)

            # Move up to the parent's index
            k = k // 2

    def _sink(self, k: int) -> None:
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            k (int): The index of the element in the priority queue to sink down.
        """
        while 2 * k <= self._n:
            # Get the first child
            j = 2 * k

            # Find the smallest child
            if j < self._n and self._greater(j, j + 1):
                j += 1

            # If the parent is smaller than the smallest child, stop sinking
            if self._greater(j, k):
                break

            # Swap the parent with the smaller child
            self._exchange(k, j)

            # Move down to the child's index
            k = j

    def _greater(self, i: int, j: int) -> bool:
        """
        Compares two keys to see if the key at index i is greater than the key at index j.

        Args:
            i (int): The index of the first key to compare.
            j (int): The index of the second key to compare.

        Returns:
            bool: True if the key at index i is greater than the key at index j, False otherwise.
        """
        return self._keys[self._pq[i]] > self._keys[self._pq[j]]

    def _exchange(self, i: int, j: int) -> None:
        """
        Swaps the elements at indices i and j in the priority queue.

        Args:
            i (int): The index of the first element to swap.
            j (int): The index of the second element to swap.
        """
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
        self._qp[self._pq[i]], self._qp[self._pq[j]] = i, j

    def __bool__(self):
        """
        Returns the boolean value of the priority queue based on its size.

        Returns:
            bool: True if the priority queue is not empty, False otherwise.
        """
        return bool(self._n)


def main():
    # Initialize the priority queue with a maximum capacity
    max_n = 10
    pq = IndexMinPQ(max_n)
    
    # Insert elements into the priority queue (index, weight)
    pq.insert(0, 5)
    pq.insert(1, 10)
    pq.insert(2, 2)
    pq.insert(3, 7)
    pq.insert(4, 3)
    
    # Output the minimum element and remove it
    print(f"Minimum index before decrease_key: {pq.del_min()}")  # Expected output: 2 (index of element with key 2)
    
    # Decrease the key of an element
    pq.decrease_key(1, 1)  # Decrease key of element at index 1 to 1
    
    # Output the minimum element and remove it
    print(f"Minimum index after decrease_key: {pq.del_min()}")  # Expected output: 1 (index of element with new key 1)
    
    # Output the remaining elements in the priority queue
    while pq:
        print(f"Next minimum index: {pq.del_min()}")


if __name__ == "__main__":
    main()