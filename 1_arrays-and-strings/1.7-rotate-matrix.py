'''
1.7 Rotate Matrix:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees.
Can you do this in-place?
'''

'''
e.g. 

3 x 3 matrix

0 1 2       6 3 0
3 4 5  ==>  7 4 1
6 7 8       8 5 2

(0, 0) ==> (0, 2)
(0, 1) ==> (1, 2)
(1, 2) ==> (2, 1)
(2, 1) ==> (1, 0)

1 cycle = (0, 1) => (1, 2) => (2, 1) => (1, 0)


4 x 4 matrix

0   1   2   3       12  8   4   0
4   5   6   7   ==> 13  9   5   1
8   9   10  11      14  10  6   2
12  13  14  15      15  11  7   3

(0,1) ==> (1,3) ==> (3,2) ==> (2,0)


pattern: 
- new_x ==> old_y
- new_y ==> n - 1 - old_x
- repeat 3 times (for the 4 corners)
- each time, do for n // 2 depths:
    - (0, 0) to (0, n - 1 - depth) non inclusive
    - (1, 1) to (1, n - 1 - depth )
'''


def rotateMatrix(matrix):

    n = len(matrix)
    depths = n // 2
    print(f"original matrix = {matrix}")
    for i in range(depths):
        for j in range(i, n - 1 - i):
            curr_val = matrix[i][j]
            x, y = i, j
            for _ in range(4):
                new_x, new_y = y, n - 1 - x
                next_val = matrix[new_x][new_y]
                
                # replace next_val
                matrix[new_x][new_y] = curr_val

                # update next_val
                x, y = new_x, new_y
                curr_val = next_val
    
    print(f"rotated matrix = {matrix}")
    return matrix


# test case(s):

## 1 - 3 x 3 matrix.
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
rotateMatrix(matrix)

## 2 - 4 x 4 matrix.
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]
rotateMatrix(matrix)
                
## 3 - 5 x 5 matrix.
matrix = [[1, 2, 3, 4,5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
rotateMatrix(matrix)
                

