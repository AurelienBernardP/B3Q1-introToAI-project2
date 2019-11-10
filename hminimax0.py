# Complete this class for all parts of the project
import time
import math
from pacman_module.util import *
from pacman_module.game import Agent
from pacman_module.pacman import Directions

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.move = None


    def getNbFood(self,state):
        foodMatrix = state.getFood()
        nbFood = 0

        """Going through the matrix to count the remaining food in the game"""
        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if foodMatrix[i][j] is True:
                    nbFood += 1
        
        return nbFood

    def cut_off(self, state, depth):
        nbFoodCurrent = self.getNbFood(state)

        if(self.nbFoodPrev > nbFoodCurrent):
            self.depthMax = depth + self.depthExpansion
            self.nbFoodPrev = nbFoodCurrent

        if(depth > self.depthMax):
            return True
        else:
            return False

    def evals(self, state):
        score = state.getScore()
        foodMatrix = state.getFood()

        pacmanPosition = state.getPacmanPosition()
        ghostPosition = state.getGhostPosition(1)
        sumManhattanDist = manhattanDistance(pacmanPosition, ghostPosition)

        minDistFood = math.inf
        nbFood = 0
        """Going through the matrix to count the remaining food in the game"""
        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if (foodMatrix[i][j] is True) and (manhattanDistance((i,j), pacmanPosition )) < minDistFood:
                    minDistFood =  (manhattanDistance((i,j), pacmanPosition ))

        return score - 2 * (1/sumManhattanDist) - minDistFood * 5


    def get_action(self, state):
        # time.sleep(0.5)
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

        self.nbFoodPrev = self.getNbFood(state)
        self.depthExpansion = 3
        self.depthMax = self.depthExpansion

        try:
            self.hminimax(state, 0, 0)
            m = self.move
            # print(m)
            return m

        except IndexError:
            return Directions.STOP

    def hminimax(self, state, agent, depth):

        #Cas de base
        if (state.isWin() or state.isLose()):
            return state.getScore()
        if self.cut_off(state, depth) :
            return self.evals(state)

        max = -math.inf
        min = math.inf
        # pacman
        if(agent == 0) :
            for succ_state, succ_move in state.generatePacmanSuccessors():
                value = self.hminimax(succ_state, 1, depth + 1)
                if value > max :
                    max = value
                    if(depth == 0):
                        self.move = succ_move
            return max

        else :
            for succ_state, succ_move in state.generateGhostSuccessors(1):
                value = self.hminimax(succ_state, 0, depth+1)
                if value < min :
                    min = value
            return min
    
