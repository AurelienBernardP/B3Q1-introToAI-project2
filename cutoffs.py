# include visited state & terminal states in both cutoffs

    def cut_off(self, state, depth):

        # Terminal State
        if (state.isWin() or state.isLose()):
            return True

        # Depth limitation
        gameGrid = state.getFood()
        nbColumns = 0
        nbRows = 0
        """Going through the matrix to count the remaining food in the game"""
        for i in range(gameGrid.width):
            for j in range(gameGrid.height):
                nbColumns += 1
            nbRows += 1
        nbColumns /= nbRows

        if(depth > (nbColumns + nbRows)/5):
            return True
        else:
            return False


def cut_off(self, state, depth):
        # Terminal State
        if (state.isWin() or state.isLose()):
            return True

        # Expansion if food eaten
        nbFoodCurrent = self.getNbFood(state)
        if(self.nbFoodPrev > nbFoodCurrent):
            self.depthMax = depth + self.depthExpansion
            self.nbFoodPrev = nbFoodCurrent

        if(depth > self.depthMax):
            return True
        else:
            return False


