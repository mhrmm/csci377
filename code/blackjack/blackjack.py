#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:29:37 2018

@author: hopkinsm
"""

import random
from collections import defaultdict

    

class QLearningAgent():
  
    def __init__(self, env, epsilon=0.4, discount = 1.0, epochBatchSize=5000):
        self.qValues = defaultdict(int)
        self.env = env
        self.epsilon = epsilon
        self.discount = discount
        self.qaCount = defaultdict(int)
        self.epochBatchSize = 5000
        self.epochsSoFar = 0
        self.weights = defaultdict(int)
        self.states = {state: i for (i, state) in enumerate(self.env.getStates())}

    def go(self):
        for i in range(self.epochBatchSize):
            self.env.reset()
            while(len(self.env.getPossibleActions(self.env.getCurrentState())) > 0):
                state = self.env.getCurrentState()
                action = self.getAction(state)
                (nextState, reward) = self.env.doAction(action)
                self.update(state, action, nextState, reward)
        self.epochsSoFar += self.epochBatchSize
            
    def getWeights(self):
        return self.weights

    def getFeatures(self, state, action):
        featname = '{}-{}'.format(state,action)
        feats = {featname: 1.0}
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

    def getValue(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        return self._computeValueActionPairFromQValues(state)[0]

    def getPolicy(self, state):
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
    
        def flipCoin(eps):    
            r = random.random()
            return r < eps

        
        # Pick Action
        legalActions = self.env.getPossibleActions(state)
        
        if len(legalActions) == 0:
            return None
        elif flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.getAction(state)
            
    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        maxQ = self._computeValueActionPairFromQValues(nextState)[0]
        self.qaCount[(state, action)] += 1
        alpha = 1. / self.qaCount[(state, action)]
        multiplier = alpha * (
                reward 
                + (self.discount * maxQ) 
                - self.getQValue(state, action))
        featureVector = self.getFeatures(state, action)
        for featureName in featureVector:
            featureValue = featureVector[featureName]
            self.weights[featureName] = (self.weights[featureName] + 
                        multiplier * 
                        featureValue)




class BlackjackQLearningAgent(QLearningAgent):
    """
    def getFeatures(self, state, action):
        featname = '{}-{}'.format(state,action)
        feats = {featname: 1.0}#, str(state): 1.0}
        #if state not in set(['DONE', 'WIN', 'DRAW', 'LOSE', 'START']):            
        #    featname = 'UP{}-{}'.format(state[1],action)
        #    feats[featname] = 1.0
        #    featname = 'TOT{}-{}'.format(state[0],action)
            #feats[featname] = 1.0
        #    featname = 'UP{}'.format(state[1])     
            #feats[featname] = 1.0
        return feats
    """
    

    