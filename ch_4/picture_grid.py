grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''
print(len(grid))
newgrid = []
string = ''
for i in range(6):
    for j in range(9):
        newgrid.append(grid[j][i])
print(newgrid)

for i in range(0, len(newgrid), 9):
    #print(newgrid[i : i+9])
    print(string.join(newgrid[i : i+9]))
#print(string)
'''
def reformat(grid):
    for i in range(0,len(grid[0])): #lenth of first list in a gird
        myStr = '' # print("") break printed line after evert 2nd for loop begans
        for j in range(0,(len(grid))): # number of lists within the grid
            myStr += grid[j][i]
    print(myStr)
