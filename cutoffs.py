# include visited state & terminal states in both cutoffs



def cut_off(self, state, depth):
        foodMatrix = state.getFood()
        nbColumns = 0
        nbRows = 0

        """Going through the matrix to count the remaining food in the game"""
        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                nbColumns += 1
            nbRows += 1
        nbColumns /= nbRows

        if(depth > (nbColumns + nbRows)/2):
            return True
        else:
            return False


def cut_off(self, state, depth):
        nbFoodCurrent = self.getNbFood(state)

        if(self.nbFoodPrev > nbFoodCurrent):
            self.depthMax = depth + self.depthExpansion
            self.nbFoodPrev = nbFoodCurrent

        if(depth > self.depthMax):
            return True
        else:
            return False


