
from pacman_module.game import Agent
from pacman_module.pacman import Directions
import math
import time
from pacman_module.util import *


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
        time.sleep(0.5)
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
            m = self.moves[key(state)]
            print("move and prediction", m)
            return m

        except IndexError:
            return Directions.STOP

    def minimaxAUX(self, state, agent, closed):
        queue = Queue()
        stack = Stack()
        queue.push((state,None, 0))#(state, move to get to that state, node depth)
        ghostScores = {}
        pacmanScores = {}
        pacmanMoves = {}
        while(not queue.isEmpty()):
            (currentState, previousMove, nodeDepth) = queue.pop()
            currentKey = key(currentState)
            if(currentKey not in closed):
                closed.add(currentKey)
                #pacman turn
                if (nodeDepth % 2) == 0 :
                    if currentState.isWin() or currentState.isLose():
                        pacmanScores[currentKey] = (state.getScore())
                        continue
                    nextStates = currentState.generatePacmanSuccessors()
                    stack.push((currentState, nodeDepth))
                    for s,a in nextStates:
                        queue.push((s, a, nodeDepth + 1))
                #ghost's turn
                else :
                    if (state.isWin() or state.isLose()):
                        ghostScores[currentKey] = (state.getScore())
                        continue
                    nextStates = currentState.generateGhostSuccessors(1)
                    stack.push((currentState, nodeDepth))
                    for s,a in nextStates:
                        queue.push((s, a, nodeDepth + 1))
            else:
                if not (currentState.isWin() or currentState.isLose()):
                    if (nodeDepth % 2) == 0 :
                        pacmanScores[currentKey] = math.inf
                    else:
                        ghostScores[currentKey] = -math.inf
        
        while(not stack.isEmpty()):
            currentState, currentDepth = stack.pop()
            print("depth", currentDepth)
            if (currentDepth % 2) == 0:
                max = -math.inf
                maxMove = Directions.STOP
                for s, a in currentState.generatePacmanSuccessors():
                    succKey = key(s)
                    if(s.isWin() or s.isLose()):
                        value = s.getScore()
                        valueMove = a
                    else:
                        value = ghostScores[succKey]
                        valueMove = a
                    if max < value:
                        maxMove = a
                        max = value
                pacmanMoves[key(currentState)] = a
                pacmanScores[key(currentState)] = max
                print("max",max)
            else:
                min = math.inf
                for s, a in currentState.generateGhostSuccessors(1):
                    succKey = key(s)
                    if(s.isWin() or s.isLose()):
                        value = s.getScore()
                    else:
                        value = pacmanScores[succKey]
                    if min < value :
                        min = value
                print("min", min)
                ghostScores[key(currentState)] = min

        return pacmanMoves

    def minimax(self, state):
        closed = set()
        self.moves = self.minimaxAUX(state, 0, closed)
        print(self.moves)
        return self.moves 
    