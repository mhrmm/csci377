import random


class BlackjackEnvironment:

    def __init__(self):
        self.reset()
        self.deck = [10] * 16
        for i in range(1, 10):
            self.deck += [i] * 4
        random.shuffle(self.deck)

    def getStates(self):
        """
        Returns a list of all states.
        
        """
        states = ['DONE', 'WIN', 'DRAW', 'LOSE', 'START']
        states += [(str(cardTotal), str(upCard)) for 
                   cardTotal in range(2, 22) for 
                   upCard in range(1,11)]
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
            upCard = self.drawCard()
            result = ((str(initialTotal), str(upCard)), 0)
        elif state == 'DONE':
            raise Exception('No valid actions in state DONE.')
        elif state == 'WIN':
            result = ('DONE', 1.0)
        elif state == 'DRAW':
            result = ('DONE', 0.0)
        elif state == 'LOSE':
            result = ('DONE', -1.0)
        else:
            cardTotal = int(state[0])
            upCard = int(state[1])
            if action == 'stand':
                dealerTotal = self.getDealerTotal(upCard)
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
                    result = ((str(newCardTotal), str(upCard)), 0.0)
            else:
                raise Exception('Cannot {} in state {}.'.format(action, state))
        self.state = result[0]
        return result

    def drawCard(self):
        random.shuffle(self.deck)
        return self.deck[0]
       
    def getDealerTotal(self, upCard):
        total = upCard
        soft = False
        if upCard == 1:
            soft = True
            total = 11
        while total <= 16:
            nextCard = self.drawCard()
            if nextCard == 1:
                nextCard = 11
                soft = True
            total += nextCard
            if total > 21 and soft:
                soft = False
                total -= 10
        return total

    def reset(self):
        self.state = 'START'
