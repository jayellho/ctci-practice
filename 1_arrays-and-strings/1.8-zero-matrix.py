'''
1.8 Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to zero.
'''

'''
- matrix represented by list of lists.
- collect all zeros by iterating through entire array - O(M x N)
- store zeros:
    - list of coordinates - O(MxN)
    - list of rows and cols - O(N)
    - use matrix for storage - O(1)
- use top row and leftmost column to mark 0.
- iterate through row and column and mark accordingly.
'''

def makeZeroMatrix(matrix):

    print("original matrix:")
    for i in matrix:
        print(f"  {i}")

    # define vars.
    rows, cols = len(matrix), len(matrix[0])
    rowHasZero, colHasZero = False, False

    # collect 0th row and 0th column zeros.
    for r in range(rows):
        if matrix[r][0] == 0:
            rowHasZero = True
            break
    
    for c in range(cols):
        if matrix[0][c] == 0:
            colHasZero = True
            break
    
    # collect all other zeros.
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    
    # set zeros for coordinates for row and col starting from index 1.
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # set zeros for original 0th index row and 0th index col.
    if rowHasZero:
        for r in range(rows):
            matrix[r][0] = 0
    
    if colHasZero:
        for c in range(cols):
            matrix[0][c] = 0
                
    print("zero matrix:")
    for i in matrix:
        print(f"  {i}")
    print("================")

    return matrix


# test case(s):
## 1 - 3 x 3 matrix
matrix = [[0, 0, 0], [1,1, 1], [2, 2, 2]]
makeZeroMatrix(matrix)

## 2 - 3 x 4 matrix
matrix = [[0, 1, 1], [1, 1, 1], [2, 2, 2], [3, 3, 3]]
makeZeroMatrix(matrix)

## 3 - 4 x 5 matrix
matrix = [[1, 1, 1, 1], [0, 0, 2, 2], [3, 3, 0, 3], [4, 4, 4, 4], [5, 5, 5, 5]]
makeZeroMatrix(matrix)
