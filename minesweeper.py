from itertools import product
from copy import deepcopy

original_grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"]]

expected = [["1", "1", "2", "#", "#"],
            ["1", "#", "3", "3", "2"],
            ["2", "4", "#", "2", "0"],
            ["1", "#", "#", "2", "0"],
            ["1", "2", "2", "1", "0"] ]


def mines_adj(grid):
    row = len(grid)
    col = len(grid[0]) 
   
    if(row == 0):  
        return -1

    directions = list(product([0, 1, -1], repeat=2))
    
    newgrid = deepcopy(grid)    # make a copy of the grid that we edit
    
    for r in range(row):
        for c in range(col):
            
            if(grid[r][c] == "-"):
                count = 0
                # next code checks in all directions for a mine
                for dirs in directions:
                    nr = r + dirs[0]
                    nc = c + dirs[1]
                    
                    if 0 <= nr < row and  \
                       0 <= nc < col and grid[nr][nc] == "#":
                        count += 1
                newgrid[r][c] = str(count)  # this writes the count value into the grid location         
    return newgrid


out = mines_adj(original_grid)
# assert out == expected           # silence - because it's the same
print("This is the original grid")
for i in range(0, 5):
    print("\n", original_grid[i])

print("\nThis is the calculated grid")
for j in range(0, 5):
    print("\n", out[j])
print("\nThis is the expected grid")
for k in range(0, 5):
    print("\n", expected[k])
if out == expected:
    print("This caluclates to the same grid as expected")