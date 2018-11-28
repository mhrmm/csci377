"""
Example Bayesian network. Simplified turbo coding.

"""

from variable import Variable
from bayes import MultivariateFunction, BayesianNetwork, conditionalProb

def createMessageFunction(name):
    M1 = Variable(name, ('0', '1'))
    return MultivariateFunction([M1], {('0',): 0.5, ('1',): 0.5})

def createIdentityFunction(messageBit, encodedBit):
    M1 = Variable(messageBit, ('0', '1'))
    A1 = Variable(encodedBit, ('0', '1'))
    result = MultivariateFunction([M1, A1], {
                ('0', '0'): 1.0, 
                ('0', '1'): 0.0, 
                ('1', '0'): 0.0, 
                ('1', '1'): 1.0})
    return result


def createTransmissionFunction(messageBit, transmittedBit, noiseProb):
    M1 = Variable(messageBit, ('0', '1'))
    A1 = Variable(transmittedBit, ('0', '1'))
    result = MultivariateFunction([M1, A1], {
                ('0', '0'): 1.0 - noiseProb, 
                ('0', '1'): noiseProb, 
                ('1', '0'): noiseProb, 
                ('1', '1'): 1.0 - noiseProb})
    return result
    
def createEncodingFunction(historyBit1, historyBit2, messageBit):
    H1 = Variable(historyBit1, ('0', '1'))
    H2 = Variable(historyBit2, ('0', '1'))
    M1 = Variable(messageBit, ('0', '1'))
    result = MultivariateFunction([H1, H2, M1], {
                ('0', '0', '0'): 1.0, 
                ('0', '0', '1'): 0.0, 
                ('0', '1', '0'): 0.0, 
                ('0', '1', '1'): 1.0,
                ('1', '0', '0'): 0.0, 
                ('1', '0', '1'): 1.0, 
                ('1', '1', '0'): 1.0, 
                ('1', '1', '1'): 0.0})
    return result
    
    

NOISE_PROB = 0.1
funcs = []
funcs += [createMessageFunction('M1')]
funcs += [createMessageFunction('M2')]
funcs += [createMessageFunction('M3')]
funcs += [createMessageFunction('M4')]
funcs += [createMessageFunction('M5')]
funcs += [createIdentityFunction('M1', 'C1')]
funcs += [createIdentityFunction('M2', 'C2')]
funcs += [createIdentityFunction('M3', 'C3')]
funcs += [createIdentityFunction('M4', 'C4')]
funcs += [createIdentityFunction('M5', 'C5')]
funcs += [createIdentityFunction('M1', 'C6')]
funcs += [createIdentityFunction('M2', 'C7')]
funcs += [createIdentityFunction('M3', 'C8')]
funcs += [createIdentityFunction('M4', 'C9')]
funcs += [createIdentityFunction('M5', 'C10')]
funcs += [createIdentityFunction('M1', 'C11')]
funcs += [createIdentityFunction('M2', 'C12')]
funcs += [createIdentityFunction('M3', 'C13')]
funcs += [createIdentityFunction('M4', 'C14')]
funcs += [createIdentityFunction('M5', 'C15')]
funcs += [createTransmissionFunction('C1', 'T1', NOISE_PROB)]
funcs += [createTransmissionFunction('C2', 'T2', NOISE_PROB)]
funcs += [createTransmissionFunction('C3', 'T3', NOISE_PROB)]
funcs += [createTransmissionFunction('C4', 'T4', NOISE_PROB)]
funcs += [createTransmissionFunction('C5', 'T5', NOISE_PROB)]
funcs += [createTransmissionFunction('C6', 'T6', NOISE_PROB)]
funcs += [createTransmissionFunction('C7', 'T7', NOISE_PROB)]
funcs += [createTransmissionFunction('C8', 'T8', NOISE_PROB)]
funcs += [createTransmissionFunction('C9', 'T9', NOISE_PROB)]
funcs += [createTransmissionFunction('C10', 'T10', NOISE_PROB)]
funcs += [createTransmissionFunction('C11', 'T11', NOISE_PROB)]
funcs += [createTransmissionFunction('C12', 'T12', NOISE_PROB)]
funcs += [createTransmissionFunction('C13', 'T13', NOISE_PROB)]
funcs += [createTransmissionFunction('C14', 'T14', NOISE_PROB)]
funcs += [createTransmissionFunction('C15', 'T15', NOISE_PROB)]


bnet = BayesianNetwork(funcs)
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '1', 'T7': '0', 'T8': '1', 'T9': '0', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '1', 'T14': '0', 'T15': '0'})
print('no corrupted bits: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '1', 'T7': '1', 'T8': '1', 'T9': '0', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '1', 'T14': '0', 'T15': '0'})
print('1 corrupted bit: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '1', 'T7': '1', 'T8': '1', 'T9': '0', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '1', 'T14': '0', 'T15': '1'})
print('2 corrupted bits: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '1', 'T7': '1', 'T8': '1', 'T9': '0', 'T10': '0',                              
                              'T11': '1', 'T12': '1', 'T13': '1', 'T14': '0', 'T15': '1'})
print('3 corrupted bits: {}'.format(result))



funcs = []
funcs += [createMessageFunction('M1')]
funcs += [createMessageFunction('M2')]
funcs += [createMessageFunction('M3')]
funcs += [createMessageFunction('M4')]
funcs += [createMessageFunction('M5')]
funcs += [createIdentityFunction('M1', 'C1')]
funcs += [createIdentityFunction('M2', 'C2')]
funcs += [createIdentityFunction('M3', 'C3')]
funcs += [createIdentityFunction('M4', 'C4')]
funcs += [createIdentityFunction('M5', 'C5')]

#funcs += [createEncodingFunction('M1', 'M2', 'C1')]
#funcs += [createEncodingFunction('M2', 'M3', 'C2')]
#funcs += [createEncodingFunction('M3', 'M4', 'C3')]
#funcs += [createEncodingFunction('M4', 'M5', 'C4')]
#funcs += [createEncodingFunction('M5', 'M1', 'C5')]

funcs += [createEncodingFunction('M1', 'M3', 'C6')]
funcs += [createEncodingFunction('M2', 'M4', 'C7')]
funcs += [createEncodingFunction('M3', 'M5', 'C8')]
funcs += [createEncodingFunction('M4', 'M1', 'C9')]
funcs += [createEncodingFunction('M5', 'M2', 'C10')]
funcs += [createEncodingFunction('M1', 'M4', 'C11')]
funcs += [createEncodingFunction('M2', 'M5', 'C12')]
funcs += [createEncodingFunction('M3', 'M1', 'C13')]
funcs += [createEncodingFunction('M4', 'M2', 'C14')]
funcs += [createEncodingFunction('M5', 'M3', 'C15')]
funcs += [createTransmissionFunction('C1', 'T1', NOISE_PROB)]
funcs += [createTransmissionFunction('C2', 'T2', NOISE_PROB)]
funcs += [createTransmissionFunction('C3', 'T3', NOISE_PROB)]
funcs += [createTransmissionFunction('C4', 'T4', NOISE_PROB)]
funcs += [createTransmissionFunction('C5', 'T5', NOISE_PROB)]
funcs += [createTransmissionFunction('C6', 'T6', NOISE_PROB)]
funcs += [createTransmissionFunction('C7', 'T7', NOISE_PROB)]
funcs += [createTransmissionFunction('C8', 'T8', NOISE_PROB)]
funcs += [createTransmissionFunction('C9', 'T9', NOISE_PROB)]
funcs += [createTransmissionFunction('C10', 'T10', NOISE_PROB)]
funcs += [createTransmissionFunction('C11', 'T11', NOISE_PROB)]
funcs += [createTransmissionFunction('C12', 'T12', NOISE_PROB)]
funcs += [createTransmissionFunction('C13', 'T13', NOISE_PROB)]
funcs += [createTransmissionFunction('C14', 'T14', NOISE_PROB)]
funcs += [createTransmissionFunction('C15', 'T15', NOISE_PROB)]



bnet = BayesianNetwork(funcs)
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             #{'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'1',
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '0', 'T7': '0', 'T8': '1', 'T9': '1', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '0', 'T14': '0', 'T15': '1'})

print('no corrupted bits: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             #{'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'1',
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '0', 'T7': '1', 'T8': '1', 'T9': '1', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '0', 'T14': '0', 'T15': '1'})

print('1 corrupted parity bit: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             #{'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'1',
                             {'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '0', 'T7': '0', 'T8': '1', 'T9': '1', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '0', 'T14': '0', 'T15': '1'})

print('1 corrupted identity bit: {}'.format(result))
result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             #{'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'1',
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '0', 'T7': '1', 'T8': '1', 'T9': '1', 'T10': '0',                              
                              'T11': '1', 'T12': '0', 'T13': '0', 'T14': '0', 'T15': '0'})

print('2 corrupted parity bits: {}'.format(result))

result = conditionalProb(bnet, 
                             {'M1': '1', 'M2': '0', 'M3': '1', 'M4': '0', 'M5':'0'}, 
                             #{'T1': '1', 'T2': '1', 'T3': '1', 'T4': '0', 'T5':'1',
                             {'T1': '1', 'T2': '0', 'T3': '1', 'T4': '0', 'T5':'0',
                              'T6': '0', 'T7': '1', 'T8': '1', 'T9': '1', 'T10': '0',                              
                              'T11': '1', 'T12': '1', 'T13': '0', 'T14': '0', 'T15': '0'})

print('3 corrupted parity bits: {}'.format(result))
