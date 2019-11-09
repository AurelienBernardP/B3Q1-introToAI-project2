    import util
    def minimaxAUX(self, state, agent, closed):
        lifo = Queue()
        fifo = []
        lifo.push(state, None, 0)#(state, move to get to that state, player turn(0 pacman 1 ghost))
        while(not lifo.isEmpty()):
            (currentState, previousMove, currentPlayer) = lifo.pop()
            currentKey = key(currentState)
            if(currentKey not in closed):
                closed.add(currentKey)
                if state.isWin() or state.isLose()):
                    self.pacmanMoves[currentkey] = (previousMove, state.getScore())
                    continue
                if CurrentPlayer = 0 :
                    nextStates = currentState.generatePacmanSuccessors()
                    fifo.push(currentState, 0)
                    for s,a in nextStates:
                        lifo.push(s, a, 1)
                    
                else :
                    nextStates = currentState.generateGhostSuccessors(1)
                    for s,a in nextStates:
                        lifo.push(s, a, 0)
    def init(self, state, agent, closed, fifo, lifo):

    def getValues(self, ):