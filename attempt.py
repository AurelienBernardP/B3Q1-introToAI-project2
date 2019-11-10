from pacman_module.util import *
import math
    def minimaxAUX(self, state, agent, closed):
        queue = Queue()
        stack = Stack()
        queue.push(state, None, 0)#(state, move to get to that state, node depth)
        ghostScores = {}
        pacmanScores = {}
        pacmanMoves = {}
        while(not queue.isEmpty()):
            (currentState, previousMove, nodeDepth) = queue.pop()
            currentKey = key(currentState)
            if(currentKey not in closed):
                closed.add(currentKey)
                #pacman turn
                if nodeDepth % 2 = 0 :
                    if currentState.isWin() or currentState.isLose():
                        pacmanScores[currentKey] = (state.getScore())
                        continue
                    nextStates = currentState.generatePacmanSuccessors()
                    stack.push(currentState, nodeDepth + 1 )
                    for s,a in nextStates:
                        queue.push(s, a, 1)
                #ghost's turn
                else :
                    if state.isWin() or state.isLose()):
                        ghostScores[currentKey] = (state.getScore())
                        continue
                    nextStates = currentState.generateGhostSuccessors(1)
                    stack.push(currentState, nodeDepth + 1 )
                    for s,a in nextStates:
                        queue.push(s, a, 0)
            else:
                if not (currentState.isWin() or currentState.isLose()):
                    if nodeDepth % 2 = 0 :
                        pacmanScores[currentKey] = math.inf
                    else:
                        ghostScores[currentKey] = -math.inf
        
        while(not stack.isEmpty()):
            currentState, currentDepth = stack.pop()
            if currentDepth % 2 = 0
                max = -math.inf
                maxMove = Directions.STOP
                for s, a in currentState.generatePacmanSuccessors()
                    succKey = key(s)
                    if(s.isWin() or s.isLose()):
                        value = s.getScore()
                        valueMove = a
                    else:
                        value = ghostScores[succKey]
                        valueMove = a
                    if max < value
                        maxMove = a
                        max = value
                pacmanMoves[key(currentState)] = a
                pacmanScores[key(currentState)] = max
            else:
                min = math.inf
                for s, a in currentState.generateGhostSuccessors(1)
                    succKey = key(s)
                    if(s.isWin() or s.isLose()):
                        value = s.getScore()
                    else:
                        value = pacmanScores[succKey]
                    if min < value
                        min = value
                ghostScores[key(currentState)] = min

        return pacmanMoves
        
    def init(self, state, agent, closed, queue, stack):

    def getValues(self, ):