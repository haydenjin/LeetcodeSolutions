class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        newRowIndex = 0
        newColumnIndex = 0
        
        rowCount = 0
        columnCount = 0
        
        oneInEachRow = {}
        
        oneInEachColumn = {}
        
        oneCount = 0
        oneCountColumn = 0
        
        
        for row in grid:
            oneCount = 0
            columnCount = 0
            for number in row:
                if number == 1:
                    oneCount += 1
                columnCount += 1
            oneInEachRow.update({newRowIndex: oneCount})
            newRowIndex += 1
            rowCount += 1
        
        
        for index in range(len(grid[0])):
            results = [row[index] for row in grid]
            oneCountColumn = 0
            for item in results:
                if item == 1:
                    oneCountColumn += 1
            oneInEachColumn.update({index: oneCountColumn})        
            
        newGrid = [[0 for i in range(columnCount)] for j in range(rowCount)]
        

        newRowIndex = 0
        newColumnIndex = 0
        
        for row in range(rowCount):
            for column in range(columnCount):
                newGrid[row][column] = oneInEachRow[row] + oneInEachColumn[column] - (rowCount - oneInEachRow[row]) - (columnCount - oneInEachColumn[column])
                
                
        return newGrid
