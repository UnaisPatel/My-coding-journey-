# This program shows a grid the '#' represents a mine and the '-' represents a mine free spor
# This program also shows how many mines there are near each mine free spot

grid = [['-', '-', '#', '#', '-'],
        ['-', '#', '#', '-', '-'],
        ['#', '-', '-', '#', '-'],]

# Defining the count of mines
def count_adjacent_mines(grid):
    rows = len(grid)        # Using the len function and calculating the rows
    column = len(grid[0])   # Using the index 0 and calculating the columns
    result = [[0 for _ in range(column)] for _ in range(rows)]  # replacing each value with 0 and iterating through each value of the grid

    for i in range(rows):    # iterating through the row
        for j in range(column):     # iterating through the column
            if grid[i][j] == '#':       # using an if statement 
                result[i][j] = '#'      # if there is a mine(#) you leave the value as a #
        else:
            count = 0
            # This iterates through every cell including diagnols
            for row in range(i-1, i+2):         
                for col in range(j-1, j+2):
                    if row >= 0 and row < rows and col >= 0 and col < column and grid[row][col] == '#':     # using an if statment to determine the amount of mines near each free spot
                        count += 1
            result[i][j] = str(count)        # number of mines we calculated


    return result



print(count_adjacent_mines(grid))

