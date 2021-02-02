'''
Created on Mar 12, 2017

@author: Jonat
'''
import sys

class AdversarialSearch():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def minimax(self):
        '''
        '''
    
    def terminalTest(self, state):
        childrenList = state.getChildren()
        if len(childrenList) != 0:
            return False
        return True

    def minimize(self, state, alpha, beta):
        if (self.terminalTest(state)):
            return (state, state.eval())
        minTuple = (None, sys.maxsize)
        childrenList = state.getChildren()
        for child in childrenList:
            currentMaxTuple = self.maximize(child, alpha, beta)
            if currentMaxTuple[1] < minTuple[1]:
                minTuple = currentMaxTuple
            if minTuple[1] >= alpha:
                break
            if minTuple[1] < beta:
                beta = minTuple[1]
        return minTuple
    
    def maximize(self, state, alpha, beta):
        if (self.terminalTest(state)):
            return (state, state.eval())
        maxTuple = (None, -sys.maxsize - 1)
        childrenList = state.getChildren()
        if len(childrenList) != 0:
            for child in childrenList:
                currentMinTuple = self.minimize(child, alpha, beta)
                if currentMinTuple[1] > maxTuple[1]:
                    maxTuple = currentMinTuple
                if maxTuple[1] >= beta:
                    break
                if maxTuple[1] > alpha:
                    alpha = maxTuple[1]
        return maxTuple
        
    def decision(self, state):
        maximum = self.maximize(state, -sys.maxsize - 1, sys.maxsize)
        return maximum
