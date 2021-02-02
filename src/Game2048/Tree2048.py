'''
Created on Mar 25, 2017

@author: Jonat
'''


vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)
maxDepth = 2

class State2048(object):

    def __init__(self, grid, depth, minOrMax, parentToChildDirection, parentToChildTile):
        self.grid = grid
        self.depth = depth
        self.parentToChildDirection = parentToChildDirection  # for min to max
        self.parentToChildTile = parentToChildTile  # for min to max
        countUniqueNumbersAndSumTuple = self.countUniqueNumbersAndSum(grid)
        self.heuristic = (-0.01 * (2048 - grid.getMaxTile())) + (10 * len(grid.getAvailableCells())) + (10 * len(grid.getAvailableMoves())) + (-4*countUniqueNumbersAndSumTuple[0]) + 2*countUniqueNumbersAndSumTuple[1]
        if (minOrMax == "MAX"):
            moves = grid.getAvailableMoves()
            childrenList = []
            if depth < maxDepth:
                for move in moves:
                    newMoveGrid = grid.clone()
                    newMoveGrid.move(vecIndex[move])
                    newDepth = depth + 1
                    childrenList.append(State2048(newMoveGrid, newDepth, "MIN", move, parentToChildTile))
                self.children = childrenList
            else:
                self.children = []
        elif(minOrMax == "MIN"):
            childrenList = []
            cells = grid.getAvailableCells()
            for cell in cells:
                # 2
                newOpponentGrid2 = grid.clone()
                newOpponentGrid2.setCellValue(cell, 2)
                if depth < maxDepth:
                    newDepth = depth + 1
                    childrenList.append(State2048(newOpponentGrid2, newDepth, "MAX", parentToChildDirection, (cell, 2)))
                else:
                    self.children = []
                # 4
                newOpponentGrid4 = grid.clone()
                newOpponentGrid4.setCellValue(cell, 4)
                if depth < maxDepth:
                    newDepth = depth + 1
                    childrenList.append(State2048(newOpponentGrid4, newDepth, "MAX", parentToChildDirection, (cell, 4)))
                else:
                    self.children = []
                self.children = childrenList
                
    def eval(self):
        return self.heuristic

    def getParentToChildDirection(self):
        return self.parentToChildDirection
    
    def getChildren(self):
        return self.children
    
    def getDepth(self):
        return self.depth
    
    def countUniqueNumbersAndSum(self, grid):
        i = 0
        j = 0
        cellValueSet = set()
        sum = 0
        while i < 4:
            while j < 4:
                cellValue = grid.getCellValue((i,j))
                cellValueSet.add(cellValue)
                sum = sum + cellValue
                j = j + 1
            i = i + 1
        return (len(cellValueSet), sum)    