"""
Example Bayesian network. P(P="yes" | S="-ve", B="-ve", U="-ve") = 0.1021.

"""

from variable import Variable
from bayes import MultivariateFunction, BayesianNetwork, conditionalProb


P = Variable('P', ['yes', 'no'])
L = Variable('L', ['u', 'd'])
S = Variable('S', ['-ve', '+ve'])
B = Variable('B', ['-ve', '+ve'])
U = Variable('U', ['-ve', '+ve'])
fP = MultivariateFunction([P], {
        ('yes',): 0.87, 
        ('no',): 0.13})
fL = MultivariateFunction([P, L], {
        ('yes', 'u'): 0.1, 
        ('yes', 'd'): 0.9, 
        ('no', 'u'): 0.99, 
        ('no', 'd'): 0.01})
fS = MultivariateFunction([P, S], {
        ('yes', '-ve'): 0.1, 
        ('yes', '+ve'): 0.9, 
        ('no', '-ve'): 0.99, 
        ('no', '+ve'): 0.01})
fB = MultivariateFunction([L, B], {
        ('u', '-ve'): 0.9, 
        ('u', '+ve'): 0.1, 
        ('d', '-ve'): 0.3, 
        ('d', '+ve'): 0.7})
fU = MultivariateFunction([L, U], {
        ('u', '-ve'): 0.9, 
        ('u', '+ve'): 0.1, 
        ('d', '-ve'): 0.2, 
        ('d', '+ve'): 0.8})
bnet = BayesianNetwork([fP, fL, fS, fB, fU])
result = conditionalProb(bnet, {'P': 'yes'}, {'S': '-ve', 'B': '-ve', 'U': '-ve'})
print(result)

