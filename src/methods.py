CELL_GRID_RATIO = 10

def screenSize(path):
    with open(path, "r", encoding="utf-8") as f:
        height = 0
        width = 0

        for line in f:
            if not width:
                for c in line:
                    width+=1
            height+=1
    return height*CELL_GRID_RATIO, width*CELL_GRID_RATIO

def readGridFile(path):
    with open(path, "r", encoding="utf-8") as f:
        l = []
        i = 0
        j = 0

        while True:
            c = f.read(1)

            if not c:
                return l
            elif c == "\n":
                j+=1
                i=0

            if c == "1":
                l.append((i,j))
            i+=1
        

def greedToScreen(position):
    x = position[0]*CELL_GRID_RATIO
    y = position[1]*CELL_GRID_RATIO
    return (x, y, CELL_GRID_RATIO, CELL_GRID_RATIO)