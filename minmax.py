
from pacman_module.game import Agent
from pacman_module.pacman import Directions
import math
import time


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
        
    def get_action(self, state):
        time.sleep(1)
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
            self.moves = self.minimax(state)

        try:
            m = self.moves[key(state)][0]
            print("move and prediction", m,self.moves[key(state)][1])
            return m

        except IndexError:
            return Directions.STOP

    def minimaxAUX(self, state, agent, closed):
        """
        Given a pacman game state,
        returns a list of legal moves to solve the search layout.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A list of legal moves as defined in `game.Directions`.
        """
        max = -math.inf
        min = math.inf

        current_key = key(state)
        if current_key in closed :
            if(agent == 0):
                self.moves[current_key] = (Directions.STOP, -math.inf)
                return -math.inf
            else :
                return math.inf
        closed.add(current_key)

        #Cas de base
        if state.isWin() or state.isLose():
            return state.getScore()

        # pacman
        if(agent == 0) :
            value = -math.inf
            value_move = Directions.STOP
            for succ_state, succ_move in state.generatePacmanSuccessors():
                value = self.minimaxAUX(succ_state, 1, closed)
                if value > max :
                    max = value
                    value_move = succ_move
                    
            self.moves[current_key] = (value_move, max)
            #end for
            print("Return ", max)
            return max

        else :
            value = math.inf
            for succ_state, succ_move in state.generateGhostSuccessors(1):
                value = self.minimaxAUX(succ_state, 0, closed)
                if value < min :
                    min = value

            return min

    def minimax(self, state):
        closed = set()
        max = self.minimaxAUX(state, 0, closed)
        print(self.moves)
        return self.moves 
    