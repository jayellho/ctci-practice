# Extracted from "The Algorithm Design Manual" pages 440-444

## Considerations for choosing the right data structure for implementing a dictionary:
1. How many items?
   1. Known in advance?
   2. Small such that a simple data structure suffices?
   3. Large such that we may worry about running out of memory or virtual memory performance?
2. Relative frequencies of insert, delete, and search operations?
   1. Static data structures (e.g. sorted arrays): good enough where no modifications after first constructed.
   2. Semi-dynamic data structures (support insrtion but not deletion): can have much simpler implementations than fully dynamic ones.
3. Access patterns of keys - uniform and random?
   1. Search queries - tend to have a skewed access distribution
   2. Queries also tend to have clustered access distribution
   3. Splay tree is a data structure that takes advantage of these skewed and clustered properties.
4. Critical that each individual operation is fast OR that the total amount of work done over the entire program be minimized?

## Underlying data structures for implementing a dictionary:
1. Unsorted linked lists or arrays
   1. Unsorted array - easiest to maintain for small datasets.
   2. Linked structures - terrible cache performance compared with arrays.
   3. Self-organizing list: When key is accessed or inserted, move it to head of list. Helps with search in future - average time for search is much better with this.
      1. Can be built with arrays, linked lists or trees.
2. Sorted linked lists or arrays
   1. Sorted linked list - usually not worth unless trying to eliminate duplicates because cannot run binary search on linked list.
   2. Sorted array - appropriate iff not many insertions or deletions.
3. Hash tables
   1. Good for moderate-to-large number of keys.
   2. How does it look like:
      1. Hash function to map keys to integers between 0 and m-1.
      2. Maintain array of m buckets - each usually an unsorted linked list.
   3. Key considerations:
      1. How to deal with collisions?
         1. Open addressing
         2. Bucketing
      2. How big should the table be?
         1. Open addressing - 30% to 50% larger; using a prime number as m minimizes dangers of a bad hash function.
         2. Bucketing - same as max num of items to be put into table.
      3. What hash function to use?
4. Binary search trees
5. B-trees
6. Skip lists
