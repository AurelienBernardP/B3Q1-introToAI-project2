from pacman_module.util import *
from pacman_module.game import Agent
from pacman_module.pacman import Directions
import math


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
    return (state.getPacmanPosition(), state.getFood(),
            state.getGhostPosition(1), state.getGhostDirection(1))


def cutOff(state, depth):
    """
    Indicates if the state should expand or not.

    Arguments:
    ----------
    - `state`: the current game state. See class `pacman.GameState`.
    - `depth`: the depth of 'state' compared to the initial state

    Return:
    -------
    - A boolean which is true if the state should stop expanding.
    """
    if (state.isWin() or state.isLose()):
        return True
    gameGrid = state.getFood()
    # Going through the game to count the number of rows and columns
    nbRows = gameGrid.width
    nbColumns = gameGrid.height
    if(depth > (nbColumns + nbRows)/6):
        return True
    else:
        return False


def evals(state):
    """
    Returns an estimation of the utility function for the given state

    Arguments:
    ----------
    - `state`: the current game state. See class `pacman.GameState`.

    Return:
    -------
    - A real number which represents the estimation of the utility
    function for the given state.
    """
    if (state.isWin() or state.isLose()):
            return state.getScore()
    score = state.getScore()
    gameGrid = state.getFood()
    pacmanPosition = state.getPacmanPosition()
    sumManhattanDist = 0
    # Summing the manhattan distances between Pacman and all food
    for i in range(gameGrid.width):
        for j in range(gameGrid.height):
            if gameGrid[i][j] is True:
                sumManhattanDist += manhattanDistance(pacmanPosition, (i, j))

    return score - sumManhattanDist


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.move = None

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
            return self.move

        except IndexError:
            return Directions.STOP

    def hminimax(self, state, agent, depth):
        """
        Returns the best payoff for the current agent 'agent'
        while attempting to predict the moves of the other agent
        within a range.
        It also defines the optimal next move within that range

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.
        - 'agent': agent who has the move in the given 'state'
        - 'depth': the depth of 'state' compared to the
                   initial state

        Return:
        -------
        - Returns the payoff explained above
        """
        if cutOff(state, depth):
            return evals(state)
        max = -math.inf
        min = math.inf

        # Pacman has the move
        if agent == 0:
            for succState, succMove in state.generatePacmanSuccessors():
                value = self.hminimax(succState, 1, depth+1)
                if value > max:
                    max = value
                    if depth == 0:
                        self.move = succMove
            return max
        # Ghost has the move
        else:
            for succState, succMove in state.generateGhostSuccessors(1):
                value = self.hminimax(succState, 0, depth+1)
                if value < min:
                    min = value
            return min
