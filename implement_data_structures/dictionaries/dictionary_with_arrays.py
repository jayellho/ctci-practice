from __future__ import annotations

class UnsortedArrDictionary:
    def __init__(self):
        self.dictionary = []

    def search(self, k): # O(n)
        for idx, (key,val) in enumerate(self.dictionary):
            if k == key:
                return idx
        return None
        
    def insert(self, k, v): # O(1)
        self.dictionary.append((k,v))

    def delete(self, x): # assumption: given a pointer to the index, so no need to search. hack is to move last item in list to that empty spot. so it will be O(1)
        if not self.dictionary:
            return
        if self.dictionary[x] == self.dictionary[-1]:
            self.dictionary.pop()
        else:
            replace = self.dictionary.pop()
            self.dictionary[x] = replace
        
    def max(self):
        if not self.dictionary:
            return None
        curr_max = self.dictionary[0][0]

        for k, v in self.dictionary:
            curr_max = max(curr_max, k)
        return curr_max

    def min(self):
        if not self.dictionary:
            return None
        curr_min = self.dictionary[0][0]
        
        for k, v in self.dictionary:
            curr_min = min(curr_min, k)
        return curr_min

    def predecessor(self, x):

        if not self.dictionary:
            return None
        curr_k = self.dictionary[x][0]
        pred = None
        pred_idx = None

        for idx, (k, v) in enumerate(self.dictionary):
            if k < curr_k:  # First, check if k is a valid predecessor
                if pred is None or k > pred:  # Then check if it's better than current best
                    pred = k
                    pred_idx = idx
        return pred_idx if pred_idx is not None else None

    def successor(self, x):
        if not self.dictionary:
            return None
        curr_k = self.dictionary[x][0]
        succ = None
        succ_idx = None

        for idx, (k, v) in enumerate(self.dictionary):
            if k > curr_k:  # First, check if k is a valid successor
                if succ is None or k < succ:  # Then check if it's better than current best
                    succ = k
                    succ_idx = idx
        return succ_idx if succ_idx is not None else None
    
    def print_dict(self):
        """Helper method to visualize the dictionary."""
        if not self.dictionary:
            print("Dictionary is empty")
            return
        print("\nCurrent Dictionary:")
        for idx, (k, v) in enumerate(self.dictionary):
            print(f"  Index {idx}: key={k}, value={v}")

class SortedArrDictionary:
    def __init__(self):
        self.dictionary = []

    def search(self, k): # O(log n)
        low, high = 0, len(self.dictionary)-1

        while low <= high:
            mid = (low + high) // 2

            if self.dictionary[mid][0] < k:
                low = mid + 1
            elif self.dictionary[mid][0] > k:
                high = mid - 1
            else:
                return mid
        return None

    def insert(self, k, v):
        # Check if key already exists (update if so)
        for idx, (key, val) in enumerate(self.dictionary):
            if key == k:
                self.dictionary[idx] = (k, v)  # Update existing
                return
            elif key > k:
                # Found insertion point
                self.dictionary.insert(idx, (k, v))
                return
        
        # If we get here, k is larger than all existing keys
        self.dictionary.append((k, v))

    def delete(self, x):
        if not self.dictionary or x < 0 or x >= len(self.dictionary):
            return
        self.dictionary.pop(x)


    def max(self):
        if not self.dictionary:
            return None
        return self.dictionary[-1][0]

    def min(self):
        if not self.dictionary:
            return None
        return self.dictionary[0][0]

    def predecessor(self, x):
        if not self.dictionary or x <= 0 or x >= len(self.dictionary):
            return None
        return x - 1

    def successor(self, x):
        if not self.dictionary or x < 0 or x >= len(self.dictionary) - 1:
            return None
        return x + 1
    
    def print_dict(self):
        """Helper method to visualize the dictionary."""
        if not self.dictionary:
            print("Dictionary is empty")
            return
        print("\nCurrent Dictionary (sorted by key):")
        for idx, (k, v) in enumerate(self.dictionary):
            print(f"  Index {idx}: key={k}, value={v}")
    
# driver code.
if __name__ == "__main__":
    d = UnsortedArrDictionary()
    
    print("=" * 50)
    print("UNSORTED ARRAY DICTIONARY DEMO")
    print("=" * 50)
    
    # Test Insert (O(1))
    print("\n### INSERT (O(1)) ###")
    d.insert(5, "five")
    d.insert(2, "two")
    d.insert(8, "eight")
    d.insert(1, "one")
    d.insert(9, "nine")
    d.insert(4, "four")
    d.print_dict()
    
    # Test duplicate insertion
    print("\n### INSERT DUPLICATE (allowed) ###")
    d.insert(5, "FIVE_DUPLICATE")
    d.print_dict()
    print("Note: Duplicates are allowed!")
    
    # Test Search (O(n))
    print("\n### SEARCH (O(n)) ###")
    idx = d.search(8)
    print(f"Search for key 8: found at index {idx}")
    if idx is not None:
        print(f"  Value: {d.dictionary[idx][1]}")
    
    idx = d.search(5)
    print(f"Search for key 5: found at index {idx}")
    print(f"  Value: {d.dictionary[idx][1]} (returns first occurrence)")
    
    idx = d.search(99)
    print(f"Search for key 99: {idx} (not found)")
    
    # Test Min/Max (O(n))
    print("\n### MIN/MAX (O(n)) ###")
    print(f"Minimum key: {d.min()}")
    print(f"Maximum key: {d.max()}")
    
    # Test Predecessor/Successor (O(n))
    print("\n### PREDECESSOR/SUCCESSOR (O(n)) ###")
    target_idx = d.search(5)
    print(f"Target: index {target_idx}, key={d.dictionary[target_idx][0]}")
    
    pred_idx = d.predecessor(target_idx)
    if pred_idx is not None:
        print(f"Predecessor: index {pred_idx}, key={d.dictionary[pred_idx][0]}")
    else:
        print("Predecessor: None (this is the smallest key)")
    
    succ_idx = d.successor(target_idx)
    if succ_idx is not None:
        print(f"Successor: index {succ_idx}, key={d.dictionary[succ_idx][0]}")
    else:
        print("Successor: None (this is the largest key)")
    
    # Test on minimum element
    print("\n### PREDECESSOR/SUCCESSOR of MIN ###")
    min_idx = d.search(d.min())
    print(f"Min element: index {min_idx}, key={d.dictionary[min_idx][0]}")
    pred_idx = d.predecessor(min_idx)
    print(f"Predecessor of min: {pred_idx} (should be None)")
    succ_idx = d.successor(min_idx)
    if succ_idx is not None:
        print(f"Successor of min: index {succ_idx}, key={d.dictionary[succ_idx][0]}")
    
    # Test Delete (O(1))
    print("\n### DELETE (O(1)) ###")
    print("Before delete:")
    d.print_dict()
    
    delete_idx = 1
    print(f"\nDeleting index {delete_idx} (key={d.dictionary[delete_idx][0]})...")
    d.delete(delete_idx)
    print("After delete:")
    d.print_dict()
    print("Note: Last element moved to the deleted position")
    
    # Delete another element
    delete_idx = 0
    print(f"\nDeleting index {delete_idx} (key={d.dictionary[delete_idx][0]})...")
    d.delete(delete_idx)
    print("After delete:")
    d.print_dict()
    
    # Summary
    print("\n" + "=" * 50)
    print("TIME COMPLEXITY SUMMARY")
    print("=" * 50)
    print("Search(k):           O(n)")
    print("Insert(k, v):        O(1)  ← Duplicates allowed")
    print("Delete(index):       O(1)  ← Requires index, not key")
    print("Min():               O(n)")
    print("Max():               O(n)")
    print("Predecessor(index):  O(n)")
    print("Successor(index):    O(n)")


    d = SortedArrDictionary()
    
    print("=" * 50)
    print("SORTED ARRAY DICTIONARY DEMO")
    print("=" * 50)
    
    # Test Insert (O(n))
    print("\n### INSERT (O(n)) ###")
    print("Inserting: 5, 2, 8, 1, 9, 4")
    d.insert(5, "five")
    d.insert(2, "two")
    d.insert(8, "eight")
    d.insert(1, "one")
    d.insert(9, "nine")
    d.insert(4, "four")
    d.print_dict()
    print("Note: Array stays sorted after each insertion!")
    
    # Test updating existing key
    print("\n### UPDATE EXISTING KEY ###")
    print("Updating key 5 to 'FIVE'")
    d.insert(5, "FIVE")
    d.print_dict()
    print("Note: No duplicates - key 5 was updated, not added")
    
    # Test Search (O(log n))
    print("\n### SEARCH (O(log n) - Binary Search) ###")
    idx = d.search(8)
    print(f"Search for key 8: found at index {idx}")
    if idx is not None:
        print(f"  Value: {d.dictionary[idx][1]}")
    
    idx = d.search(1)
    print(f"Search for key 1: found at index {idx}")
    if idx is not None:
        print(f"  Value: {d.dictionary[idx][1]}")
    
    idx = d.search(99)
    print(f"Search for key 99: {idx} (not found)")
    
    # Test Min/Max (O(1))
    print("\n### MIN/MAX (O(1)) ###")
    print(f"Minimum key: {d.min()} (first element)")
    print(f"Maximum key: {d.max()} (last element)")
    
    # Test Predecessor/Successor (O(1))
    print("\n### PREDECESSOR/SUCCESSOR (O(1)) ###")
    target_idx = d.search(5)
    print(f"Target: index {target_idx}, key={d.dictionary[target_idx][0]}")
    
    pred_idx = d.predecessor(target_idx)
    if pred_idx is not None:
        print(f"Predecessor: index {pred_idx}, key={d.dictionary[pred_idx][0]}")
    else:
        print("Predecessor: None")
    
    succ_idx = d.successor(target_idx)
    if succ_idx is not None:
        print(f"Successor: index {succ_idx}, key={d.dictionary[succ_idx][0]}")
    else:
        print("Successor: None")
    
    # Test on boundaries
    print("\n### PREDECESSOR/SUCCESSOR AT BOUNDARIES ###")
    min_idx = 0
    print(f"Min element: index {min_idx}, key={d.dictionary[min_idx][0]}")
    print(f"Predecessor of min: {d.predecessor(min_idx)} (should be None)")
    succ_idx = d.successor(min_idx)
    if succ_idx is not None:
        print(f"Successor of min: index {succ_idx}, key={d.dictionary[succ_idx][0]}")
    
    max_idx = len(d.dictionary) - 1
    print(f"\nMax element: index {max_idx}, key={d.dictionary[max_idx][0]}")
    pred_idx = d.predecessor(max_idx)
    if pred_idx is not None:
        print(f"Predecessor of max: index {pred_idx}, key={d.dictionary[pred_idx][0]}")
    print(f"Successor of max: {d.successor(max_idx)} (should be None)")
    
    # Test Delete (O(n))
    print("\n### DELETE (O(n)) ###")
    print("Before delete:")
    d.print_dict()
    
    delete_idx = d.search(2)
    print(f"\nDeleting index {delete_idx} (key={d.dictionary[delete_idx][0]})...")
    d.delete(delete_idx)
    print("After delete:")
    d.print_dict()
    print("Note: Elements shift left to fill the gap")
    
    # Traverse in sorted order using predecessor/successor
    print("\n### TRAVERSE IN SORTED ORDER ###")
    print("Using Min and Successor to iterate:")
    idx = 0  # Start from minimum
    keys_in_order = []
    while idx is not None:
        keys_in_order.append(d.dictionary[idx][0])
        idx = d.successor(idx)
    print(f"Keys in order: {keys_in_order}")
    
    # Summary
    print("\n" + "=" * 50)
    print("TIME COMPLEXITY SUMMARY")
    print("=" * 50)
    print("Search(k):           O(log n) ← Binary search!")
    print("Insert(k, v):        O(n)     ← Must maintain order")
    print("Delete(index):       O(n)     ← Must shift elements")
    print("Min():               O(1)     ← First element")
    print("Max():               O(1)     ← Last element")
    print("Predecessor(index):  O(1)     ← Just index - 1")
    print("Successor(index):    O(1)     ← Just index + 1")
    print("\n" + "=" * 50)
    print("COMPARISON: Sorted vs Unsorted Array")
    print("=" * 50)
    print("Operation       | Unsorted | Sorted")
    print("----------------|----------|----------")
    print("Search          | O(n)     | O(log n) ✓")
    print("Insert          | O(1) ✓   | O(n)")
    print("Delete          | O(1) ✓   | O(n)")
    print("Min/Max         | O(n)     | O(1) ✓")
    print("Predecessor     | O(n)     | O(1) ✓")
    print("Successor       | O(n)     | O(1) ✓")