#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:29:37 2018

@author: hopkinsm
"""

import environment
import random
import util


    
    
class BlackjackEnvironment(environment.Environment):

    def __init__(self):
        self.reset()
        self.deck = [10] * 16
        for i in range(1, 10):
            self.deck += [i] * 4
        random.shuffle(self.deck)

    def getStates(self):
        """
        Return list of all states.
        
        """
        # The true terminal state.
        states = ['DONE', 'WIN', 'DRAW', 'LOSE', 'START']
        states += [str(cardTotal) for cardTotal in range(2, 22)]
        return states

    def getCurrentState(self):
        return self.state

    def getPossibleActions(self, state):
        if state == 'DONE':
            return ()
        elif state == 'START':
            return ('deal',)
        elif state in ['WIN', 'DRAW', 'LOSE']:
            return ('done',)
        else:
            return ('hit','stand')
    

    def doAction(self, action):
        state = self.getCurrentState()
        if state == 'START':
            if action != 'deal':
                raise Exception('Cannot {} in state START.'.format(action))
            initialTotal = self.drawCard() + self.drawCard()
            result = (str(initialTotal), 0)
        elif state == 'DONE':
            raise Exception('No valid actions in state DONE.')
        elif state == 'WIN':
            result = ('DONE', 1.0)
        elif state == 'DRAW':
            result = ('DONE', 0.0)
        elif state == 'LOSE':
            result = ('DONE', -1.0)
        else:
            cardTotal = int(state)
            if action == 'stand':
                dealerTotal = self.getDealerTotal()
                if dealerTotal > 21 or dealerTotal < cardTotal:
                    result = ('WIN', 0.0)
                elif dealerTotal == cardTotal:
                    result = ('DRAW', 0.0)
                else:
                    result = ('LOSE', 0.0)
            elif action == 'hit':
                newCardTotal = cardTotal + self.drawCard()
                if newCardTotal > 21:
                    result = ('LOSE', 0.0)
                else:
                    result = (str(newCardTotal), 0.0)
            else:
                raise Exception('Cannot {} in state {}.'.format(action, state))
        self.state = result[0]
        return result

    def drawCard(self):
        random.shuffle(self.deck)
        return self.deck[0]
       
    def getDealerTotal(self):
        total = 0
        while total <= 16:
            total += self.drawCard()
        return total

    def reset(self):
        self.state = 'START'


class QLearningAgent():
  
    def __init__(self, env, epsilon=0.4, discount = 1.0):
        "You can initialize Q-values here..."
        self.qValues = util.Counter()
        self.env = env
        self.epsilon = epsilon
        self.discount = discount

    def go(self, iters):
        self.qaCount = util.Counter()
        for i in range(iters):
            self.env.reset()
            while(len(self.env.getPossibleActions(self.env.getCurrentState())) > 0):
                state = self.env.getCurrentState()
                action = self.getAction(state)
                (nextState, reward) = self.env.doAction(action)
                self.update(state, action, nextState, reward)
        
            

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        if (state, action) not in self.qValues:
            return 0.0
        else:
            return self.qValues[(state, action)]


    def _computeValueActionPairFromQValues(self, state):
        legalActions = self.env.getPossibleActions(state)
        if len(legalActions) == 0:
            return (0.0, None)
        else:
            qVals = [self.getQValue(state, action) for action in legalActions]
            return max(zip(qVals, legalActions))

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        return self._computeValueActionPairFromQValues(state)[0]

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        return self._computeValueActionPairFromQValues(state)[1]
            

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
        """
        # Pick Action
        legalActions = self.env.getPossibleActions(state)
        
        if len(legalActions) == 0:
            return None
        elif util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)
            

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          
        """
        maxQ = self.computeValueFromQValues(nextState)
        self.qaCount[(state, action)] += 1
        alpha = 60. / (59 + self.qaCount[(state, action)])
        increment = alpha * (
                reward 
                + (self.discount * maxQ) 
                - self.getQValue(state, action))
        self.qValues[(state, action)] += increment

    def printPolicy(self):
        policy = [(state, self.getPolicy(state)) for state in self.env.getStates()]
        for (state, action) in policy:
            print('{}: {}'.format(state, action))

    def printStates(self):
        for state in self.env.getStates():
            if state != 'DONE':
                legalActions = self.env.getPossibleActions(state)
                qVals = [self.getQValue(state, action) for action in legalActions]
                print(state)
                print(zip(legalActions, qVals))
                

    def printCounts(self):
        policy = [(state, self.getPolicy(state)) for state in self.env.getStates()]
        for (state, action) in policy:
            print('{}, {}: {}'.format(state, action, self.qaCount[(state, action)]))

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class ApproxQLearningAgent(QLearningAgent):
    
    
    def __init__(self, env):
        QLearningAgent.__init__(self, env)
        self.weights = util.Counter()
        self.states = {state: i for (i, state) in enumerate(self.env.getStates())}
        
    def getWeights(self):
        return self.weights

    def getFeatures(self, state, action):
        feats = {str((state, action)): 1.0}#, str(state): 1.0}
        if state not in set(['DONE', 'WIN', 'DRAW', 'LOSE', 'START']):
            #feats['total'] = int(state)
            cardTotal = int(state)
            if cardTotal < 17:
                feats['lt17{}'.format(action)] = 1.0
            if cardTotal < 12:
                feats['lt12{}'.format(action)] = 1.0
            if cardTotal >= 12:
                feats['gt12{}'.format(action)] = 1.0
            if cardTotal >= 17:
                feats['gt17{}'.format(action)] = 1.0
            #if cardTotal >= 16:
            #    feats['gt16{}'.format(action)] = 1.0
            #if cardTotal >= 15:
            #    feats['gt15{}'.format(action)] = 1.0

            #for i in range(cardTotal, 22):
            #    featureName = 'lt{}'.format(i)
            #    feats[featureName] = 1.0       
        #print(feats)
        return feats

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        featureVector = self.getFeatures(state, action)
        dotProduct = 0.0
        for featureName in self.weights:
            if featureName in featureVector:
                weight = self.weights[featureName]
                featureValue = featureVector[featureName]
                dotProduct += weight * featureValue
        return dotProduct
            
    def _computeValueActionPairFromQValues(self, state):
        legalActions = self.env.getPossibleActions(state)
        if len(legalActions) == 0:
            return (0.0, None)
        else:
            qVals = [self.getQValue(state, action) for action in legalActions]
            return max(zip(qVals, legalActions))


    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        maxQ = self._computeValueActionPairFromQValues(nextState)[0]
        self.qaCount[(state, action)] += 1
        alpha = 60. / (59 + self.qaCount[(state, action)])

        multiplier = alpha * (
                reward 
                + (self.discount * maxQ) 
                - self.getQValue(state, action))
        featureVector = self.getFeatures(state, action)
        for featureName in featureVector:
            featureValue = featureVector[featureName]
            self.weights[featureName] = self.weights[featureName] + multiplier * featureValue



env = BlackjackEnvironment()
agent = ApproxQLearningAgent(env)
agent.go(200000)
agent.printPolicy()
agent.printStates()
