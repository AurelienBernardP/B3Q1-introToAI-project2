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

    # Manhattan distance between Pacman and Ghost
    pacmanPosition = state.getPacmanPosition()
    ghostPosition = state.getGhostPosition(1)
    distGhostPacman = manhattanDistance(pacmanPosition, ghostPosition)

    # Manhattan distance between Pacman and the closest food
    score = state.getScore()
    gameGrid = state.getFood()
    minDistFood = math.inf
    nbFood = 0
    for i in range(gameGrid.width):
        for j in range(gameGrid.height):
            if gameGrid[i][j] is True:
                nbFood += 1
                manhattanDist = manhattanDistance((i, j), pacmanPosition)
                if manhattanDist < minDistFood:
                    minDistFood = manhattanDist

    return 3*score + 2*distGhostPacman - 5*minDistFood - 40*nbFood


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
