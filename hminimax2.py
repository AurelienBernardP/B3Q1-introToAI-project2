# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args


    def cut_off(self, state):
        foodMatrix = state.getFood()
        pacmanPosition = state.getPacmanPosition()
        nbFood = 0
        nbCells = 0
        sumManhattanDist = 0

        """Going through the matrix to count the remaining food in the game"""
        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if foodMatrix[i][j] is True:
                    sumManhattanDist += manhattanDistance(pacmanPosition, (i, j))
                    nbFood += 1
            nbCells += 1
        if(nbFood != 0):
            meanMDFood = sumManhattanDist / nbFood
        else:
            meanMDFood = 0

        if(meanMDFood >= (math.sqrt(nbCells))):
            return True
        else:
            return False


    def evals(self, state):
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


    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        return Directions.STOP
