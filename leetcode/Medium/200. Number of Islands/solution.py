class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def addAdjacents(i, j, queue):
            if i > 0:
                if grid[i-1][j] == "1":
                    queue.append([i-1,j])
            if i < len(grid)-1:
                if grid[i+1][j] == "1":
                    queue.append([i+1,j])
            if j > 0:
                if grid[i][j-1] == "1":
                    queue.append([i,j-1])
            if j < len(grid[0])-1:
                if grid[i][j+1] == "1":
                    queue.append([i,j+1])

        numIslands = 0
        running = True
        while running:
            running = False  # When no 1 is found after searching the whole grid, then the while loop stops

            queue = []
            # Iterate through grid in search of 1
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "1":
                        running = True
                        numIslands += 1

                        addAdjacents(i, j, queue)
                        grid[i][j] = "0"
                        while queue != []:
                            coord = queue.pop()
                            if grid[coord[0]][coord[1]] == "1":
                                addAdjacents(coord[0], coord[1], queue)
                                grid[coord[0]][coord[1]] = "0"
                                queue = [x for x in queue if x != coord]

        return numIslands
