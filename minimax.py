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


class PacmanAgent(Agent):
    """
    A Pacman agent based on Depth-First-Search.
    """
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.moves = {}
        self.closed = set()

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

        if key(state) not in self.moves:
            self.minimax(state, 0)

        try:
            return self.moves[key(state)][0]

        except IndexError:
            return Directions.STOP

    def minimax(self, state, agent):
        """
        Returns the best payoff for the current agent 'agent'
        while predicting the moves of the other agent.
        It also defines the optimal next move for Pacman given 'state'

        Arguments:
        ----------
        - `state`: the current game state. See class `pacman.GameState`.
        - 'agent': agent who has the move in the given 'state'

        Return:
        -------
        - Returns the payoff explained above
        """
        current_key = key(state)
        if current_key in self.closed:
            if not (state.isWin() or state.isLose()):
                if agent == 0:
                    return -math.inf
                else:
                    return math.inf
            else:
                return state.getScore()
        self.closed.add(current_key)
        max = -math.inf
        min = math.inf

        # Pacman has the move
        if agent == 0:
            if state.isWin() or state.isLose():
                return state.getScore()
            value_move = Directions.STOP
            for succ_state, succ_move in state.generatePacmanSuccessors():
                value = self.minimax(succ_state, 1)
                if value > max:
                    max = value
                    value_move = succ_move
            self.moves[current_key] = (value_move, max)
            return max
        # Ghost has the move
        else:
            if state.isWin() or state.isLose():
                return state.getScore()
            for succ_state, succ_move in state.generateGhostSuccessors(1):
                value = self.minimax(succ_state, 0)
                if value == -math.inf:
                    continue
                if value < min:
                    min = value
            return min
