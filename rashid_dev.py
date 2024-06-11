def minesweeper(A):
    # Get the number of rows and columns in the matrix A
    row = len(A)
    colomn = len(A[0])

    # Convert A into a list of lists (matrix) to modify elements
    A = [list(A[i]) for i in range(row)]

    # Iterate through each element in the matrix
    for i in range(row):
        for j in range(colomn):
            # Only process non-mine cells (cells not equal to "X")
            if not A[i][j] == "X":
                counter = 0
                # Check all neighboring cells (8 possible directions)
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        try:
                            # Ensure the indices are valid and check if it's a mine ("X")
                            if not (k == -1 or l == -1) and A[k][l] == "X":
                                counter += 1
                        except IndexError:
                            # Ignore index errors (out of bounds) caused by edge cases
                            pass

                # Convert the count of neighboring mines to string and update the cell
                A[i][j] = str(counter)

    # Convert the matrix back to the desired output format (list of strings)
    A = ["".join(A[i]) for i in range(row)]

    # Return the resulting matrix
    return A


if __name__ == "__main__":

    test = [
        "XOOXXXOO",
        "OOOOXOXX",
        "XXOXXOOO",
        "OXOOOXXX",
        "OOXXXXOX",
        "XOXXXOXO",
        "OOOXOXOX",
        "XOXXOXOX",
    ]

    """Desired Output is as under
    
    ["X11XXX32", 
     "3335X5XX", 
     "XX3XX554", 
     "3X556XXX", 
     "24XXXX6X", 
     "X3XXX5X3", 
     "245X6X5X", 
     "X2XX4X4X"]
    """

    print(minesweeper(test))
