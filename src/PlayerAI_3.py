from BaseAI_3 import BaseAI
from search.AdversarialSearch import AdversarialSearch
from Game2048.Tree2048 import State2048

class PlayerAI(BaseAI):
    def getMove(self, grid):
        tree2048 = State2048(grid, 0, "MAX", None, None) #this does build out the tree
        adversarialSearch = AdversarialSearch()
        decision = adversarialSearch.decision(tree2048)
        decisionState = decision[0]
        return decisionState.getParentToChildDirection()