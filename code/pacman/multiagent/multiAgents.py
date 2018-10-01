# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

def manhattanDist(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def closestSquare(xy1, xys):
    if len(xy1) == 0:
        return None
    dists = [(manhattanDist(xy1, (x, y)), (x, y)) for (x, y) in xys]
    return min(dists)[1]

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]



    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        from search.searchAgents import ClosestDotSearchAgent
        agent = ClosestDotSearchAgent()
        if len(newFood.asList()) == 0:
            return 1000
        score = 0
        ghostDistance = min([manhattanDist(ghostState.getPosition(), newPos) for ghostState in newGhostStates])
        if ghostDistance <= 1:
            score -= 500
        #score += 15 * ghostDistance          
        if successorGameState.getScore() > currentGameState.getScore():
            score += 50
        else:
            score += 50 - 10 * len(agent.findPathToClosestDot(successorGameState))
        return score
    
    
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def _evaluateNode(self, gameState, agentIndex, depth):
        if depth == 0:
            return (self.evaluationFunction(gameState), None)
        actions = gameState.getLegalActions(agentIndex)
        successors = [gameState.generateSuccessor(agentIndex, action) for action in actions]
        nextAgentIndex = agentIndex + 1
        if nextAgentIndex >= gameState.getNumAgents():
            nextAgentIndex = 0
            depth -= 1
        evaluations = [self._evaluateNode(successor, nextAgentIndex, depth)[0] for successor in successors]
        choices = [(e,a) for (e,a) in zip(evaluations, actions) if e is not None]
        if len(choices) == 0:
            choice = (self.evaluationFunction(gameState), None)
        elif agentIndex == 0:
            choice = max(choices)
        else:
            choice = min(choices)
        return choice

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        return self._evaluateNode(gameState, 0, self.depth)[1]
            

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    
    def _evaluateNode(self, gameState, agentIndex, depth):
        if depth == 0:
            return (self.evaluationFunction(gameState), None)
        actions = gameState.getLegalActions(agentIndex)
        successors = [gameState.generateSuccessor(agentIndex, action) for action in actions]
        nextAgentIndex = agentIndex + 1
        if nextAgentIndex >= gameState.getNumAgents():
            nextAgentIndex = 0
            depth -= 1
        evaluations = [self._evaluateNode(successor, nextAgentIndex, depth)[0] for successor in successors]
        choices = [(e,a) for (e,a) in zip(evaluations, actions) if e is not None]
        if len(choices) == 0:
            choice = (self.evaluationFunction(gameState), None)
        elif agentIndex == 0:
            choice = max(choices)
        else:
            choice = min(choices)
        return choice

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self._evaluateNode(gameState, 0, self.depth)[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

