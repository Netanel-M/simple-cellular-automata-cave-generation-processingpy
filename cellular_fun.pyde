def setup():
    global grid, next_grid, cell_size, rows, columns
    cell_size = 16
    size(1220, 720)
    #fullScreen()
    grid = [[int(round(random(1))) for row in range(height/cell_size)] for column in range(width/cell_size)]
    
    rows = height/cell_size
    columns = width/cell_size

def next_gen():
    global grid
    next_grid = [[0 for x in range(height/cell_size)] for y in range(width/cell_size)]
    for row_index in range(1, rows-1):
        for column_index in range(1, columns-1):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbors += grid[column_index+i][row_index+j]
    
            neighbors -= grid[column_index][row_index]
            cell = grid[column_index][row_index]
            #print neighbors
            if cell == 1 and neighbors > 3:
               next_grid[column_index][row_index] = 1
            elif cell == 0 and neighbors > 4:
                next_grid[column_index][row_index] = 1


    grid = next_grid
    
def draw():
    noStroke()            
    for row_index in range(0, rows):
        for column_index in range(0, columns):
            if grid[column_index][row_index] == 1:
                fill(143,127,111)
            else:
                fill(112,128,144)
            rect(column_index * cell_size, row_index * cell_size, cell_size, cell_size)
def mousePressed():
    if mouseButton == CENTER:
        next_gen()        
         