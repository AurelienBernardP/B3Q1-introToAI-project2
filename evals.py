

def evals(self, state):
    if key(state) in self.closed:
        return -math.inf
    
    score = state.getScore()
    foodMatrix = state.getFood()

    pacmanPosition = state.getPacmanPosition()
    ghostPosition = state.getGhostPosition(1)
    ghostDistance = manhattanDistance(pacmanPosition, ghostPosition)

    minDistFood = math.inf
    nbFood = 0
    """Going through the matrix to count the remaining food in the game"""
    for i in range(foodMatrix.width):
        for j in range(foodMatrix.height):
            if (foodMatrix[i][j] is True): 
                nbFood +=1
                if (manhattanDistance((i,j), pacmanPosition )) < minDistFood:
                    minDistFood =  (manhattanDistance((i,j), pacmanPosition ))

    return score - 3 * (1/ghostDistance) - minDistFood*5 - nbFood * 3



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