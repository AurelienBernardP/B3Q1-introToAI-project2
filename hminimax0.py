# Complete this class for all parts of the project
import time
import math
from pacman_module.util import *
from pacman_module.game import Agent
from pacman_module.pacman import Directions

def key(state):
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

        if(depth > (nbColumns + nbRows)/6):
            return True
        else:
            return False

    def evals(self, state):
        if (state.isWin() or state.isLose()):
            return state.getScore()

        score = state.getScore()
        gameGrid = state.getFood()
        pacmanPosition = state.getPacmanPosition()
        ghostPosition = state.getGhostPosition(1)
        sumManhattanDist = 0

        """Going through the matrix to count the remaining food in the game"""
        for i in range(gameGrid.width):
            for j in range(gameGrid.height):
                if gameGrid[i][j] is True:
                    sumManhattanDist += manhattanDistance(pacmanPosition, (i, j))

        return score -  sumManhattanDist


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
        try:
            self.hminimax(state, 0, 0)
            m = self.move
            return m

        except IndexError:
            return Directions.STOP

    def hminimax(self, state, agent, depth):

        #Cas de base
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
    
