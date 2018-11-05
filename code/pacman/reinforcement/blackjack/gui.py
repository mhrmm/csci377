from pgl import GWindow, GLabel, GRect
from blackjack import BlackjackEnvironment, BlackjackQLearningAgent

GWINDOW_WIDTH = 1000               # Width of the graphics window
GWINDOW_HEIGHT = 500              # Height of the graphics window
LETTER_BASE = 10                  # Distance from bottom to the letters
WORD_BASE = 45                    # Distance from bottom to secret word
MESSAGE_BASE = 85                 # Distance from bottom to message area
SNOWMAN_BASE = 140                # Distance from bottom to Snowman base
MAX_INCORRECT_GUESSES = 8         # Number of incorrect guesses allowed
INCORRECT_COLOR = "#FF9999"       # Color used for incorrect guesses
CORRECT_COLOR = "#009900"         # Color used to mark correct guesses

# Fonts

WORD_FONT = "bold 36px 'Monaco','Monospaced'"
LETTER_FONT = "bold 24px 'Monaco','Monospaced'"
MESSAGE_FONT = "30px 'Helvetica Neue','Arial','Sans-Serif'"
gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)


env = BlackjackEnvironment()
agent = BlackjackQLearningAgent(env)

def createWindow():
 
    
    def createCardTotalLabels():
        alphabet = ['02','03','04','05','06','07','08','09','10',
                    '11','12','13','14','15','16','17','18','19',
                    '20','21']
        alphabetLabels = [GLabel(letter) for letter in alphabet]
        for label in alphabetLabels:
            label.setFont(LETTER_FONT)    
        return alphabetLabels


    def createUpCardLabels():
        alphabet = ['01','02','03','04','05','06','07','08','09','10']
        alphabetLabels = [GLabel(letter) for letter in alphabet]
        for label in alphabetLabels:
            label.setFont(LETTER_FONT)           
        return alphabetLabels
    
     
    def makeDisplay(alphabetLabels, upCardLabels):
        decisionIndicators = dict()
        letterWidth = alphabetLabels[0].getWidth()
        letterHeight = alphabetLabels[0].getHeight()
        XMARGIN = 50
        offset = (GWINDOW_WIDTH - XMARGIN -
                  (len(alphabetLabels) * letterWidth)) / (len(alphabetLabels) + 1)
        for (i, label) in enumerate(alphabetLabels):
            x = XMARGIN + (offset + letterWidth) * i + offset
            gw.add(label, x, GWINDOW_HEIGHT - LETTER_BASE)
            
        YMARGIN = 100        
        upCardOffset = (GWINDOW_HEIGHT - YMARGIN - 
                  (len(upCardLabels) * letterHeight)) / (len(upCardLabels) + 1)
        for (i, label) in enumerate(upCardLabels):
            y = YMARGIN + (upCardOffset + letterHeight) * i + upCardOffset
            gw.add(label, LETTER_BASE, y)

        for (i, upCardLabel) in enumerate(upCardLabels):
            y = YMARGIN + (upCardOffset + letterHeight) * i + upCardOffset - letterHeight
         
            for (j, totalLabel) in enumerate(alphabetLabels):
                x = XMARGIN + (offset + letterWidth) * j + offset
        
                decisionIndicator = GRect(x, y, letterHeight, letterWidth)
                decisionIndicator.setFillColor("black")
                decisionIndicator.setFilled(True)
                gw.add(decisionIndicator)
                decisionIndicators[(str(int(totalLabel.getLabel())), str(int(upCardLabel.getLabel())))] = decisionIndicator
        return decisionIndicators
            
    cardTotalLabels  = createCardTotalLabels()
    upCardLabels = createUpCardLabels()
    return makeDisplay(cardTotalLabels, upCardLabels)

decisionIndicators = createWindow()
progressLabel = GLabel("GAMES PLAYED: 0")
progressLabel.setFont(MESSAGE_FONT)
gw.add(progressLabel, 20, 50)




def adjustIndicators():
    progressLabel.setLabel('GAMES PLAYED: {}'.format(agent.epochsSoFar))
    for state in decisionIndicators:
        action = agent.getPolicy(state)
        indicator = decisionIndicators[state]
        if action == 'hit':
            indicator.setFillColor("green")
            indicator.setFilled(True)
        else:
            indicator.setFillColor("red")
            indicator.setFilled(True)

def adjustIndicatorsAlt():
    progressLabel.setLabel('GAMES PLAYED: {}'.format(agent.epochsSoFar))
    for state in decisionIndicators:
        hitValue = agent.getQValue(state, 'hit')
        standValue = agent.getQValue(state, 'stand')
        hitDifferential = hitValue - standValue
        if hitDifferential > 1:
            color = "#00FF00"
        elif hitDifferential > 0.5:
            color = "#00CC00"
        elif hitDifferential > 0.2:
            color = "#008800"
        elif hitDifferential > 0.1:
            color = "#006600"
        elif hitDifferential > 0.05:
            color = "#004400"
        elif hitDifferential > -0.05:
            color = "#000000"
        elif hitDifferential > 0.1:
            color = "#440000"
        elif hitDifferential > -0.2:
            color = "#660000"
        elif hitDifferential > -0.5:
            color = "#880000"
        elif hitDifferential > -1:
            color = "#CC0000"
        else:
            color = "#FF0000"
        indicator = decisionIndicators[state]
        indicator.setFillColor(color)
        indicator.setFilled(True)

timer1 = gw.createTimer(agent.go, 1000)
timer1.setRepeats(True)
timer1.start()
timer2 = gw.createTimer(adjustIndicatorsAlt, 1500)
timer2.setRepeats(True)
timer2.start()

  # -*- coding: utf-8 -*-

