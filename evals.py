def evals(self, state):
                # Terminal State
        if (state.isWin() or state.isLose()):
            return state.getScore()
        score = state.getScore()
        gameGrid = state.getFood()

        pacmanPosition = state.getPacmanPosition()
        ghostPosition = state.getGhostPosition(1)
        ghostDistance = manhattanDistance(pacmanPosition, ghostPosition)


        minDistFood = math.inf
        nbFood = 0
        """Going through the matrix to count the remaining food in the game"""
        for i in range(gameGrid.width):
            for j in range(gameGrid.height):
                if (gameGrid[i][j] is True): 
                    nbFood +=1
                    if (manhattanDistance((i,j), pacmanPosition )) < minDistFood:
                        minDistFood =  (manhattanDistance((i,j), pacmanPosition ))

        return score + 2 * ghostDistance - 2 * minDistFood - 4 * nbFood


def evals(self, state):

        if key(state) in self.closed:
            return -math.inf
        score = state.getScore()
        
        foodMatrix = state.getFood()
        pacmanPosition = state.getPacmanPosition()
        sumManhattanDist = 0

        """Going through the matrix to count the remaining food in the game"""
        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if foodMatrix[i][j] is True:
                    sumManhattanDist += manhattanDistance(pacmanPosition, (i, j))

        return score - 2*sumManhattanDist
