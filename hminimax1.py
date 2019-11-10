# Complete this class for all parts of the project
import time
import math
from pacman_module.util import *
from pacman_module.game import Agent
from pacman_module.pacman import Directions

def key(state):
    """
    Returns a key that uniquely identifies a Pacman game state.

    Arguments:
    ----------
    - `state`: the current game state. See FAQ and class
               `pacman.GameState`.

    Return:
    -------
    - A hashable key object that uniquely identifies a Pacman game state.
    """
    return (state.getPacmanPosition(), state.getFood(), state.getGhostPosition(1),state.getGhostDirection(1))

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.move = None


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

        if(depth > (nbColumns + nbRows)/4):
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

        try:
            self.hminimax(state, 0, 0)
            m = self.move
            # print(m)
            return m

        except IndexError:
            return Directions.STOP

    def hminimax(self, state, agent, depth):
        
        max = -math.inf
        min = math.inf

        current_key = key(state)
        if (state.isWin() or state.isLose()):
            return state.getScore()
        if self.cut_off(state, depth) :
            return self.evals(state)

        #Cas de base
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
    
