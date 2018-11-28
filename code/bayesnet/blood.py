"""
Example Bayesian network. Blood types.

"""

from variable import Variable
from bayes import MultivariateFunction, BayesianNetwork, conditionalProb

genes = ('A', 'B', 'O')
genotypes = ('AA', 'AB', 'AO', 'BB', 'BO', 'OO')
bloodtypes = ('A', 'B', 'AB', 'O')

def createGenotypePrior(name):
    V = Variable(name, genotypes)
    return MultivariateFunction([V], {
        ('AA',): 1./6, 
        ('AB',): 1./6, 
        ('AO',): 1./6, 
        ('BB',): 1./6, 
        ('BO',): 1./6, 
        ('OO',): 1./6})

def createBloodtypeDist(genotypeVar, bloodtypeVar):
    V = Variable(genotypeVar, genotypes)
    W = Variable(bloodtypeVar, bloodtypes)
    return MultivariateFunction([V, W], {
        ('AA', 'A'): 1.0,
        ('AA', 'B'): 0.0, 
        ('AA', 'AB'): 0.0, 
        ('AA', 'O'): 0.0, 
        ('AB', 'A'): 0.0,
        ('AB', 'B'): 0.0, 
        ('AB', 'AB'): 1.0, 
        ('AB', 'O'): 0.0, 
        ('AO', 'A'): 1.0,
        ('AO', 'B'): 0.0, 
        ('AO', 'AB'): 0.0, 
        ('AO', 'O'): 0.0, 
        ('BB', 'A'): 0.0,
        ('BB', 'AB'): 0.0, 
        ('BB', 'B'): 1.0, 
        ('BB', 'O'): 0.0, 
        ('BO', 'A'): 0.0,
        ('BO', 'AB'): 0.0, 
        ('BO', 'B'): 1.0, 
        ('BO', 'O'): 0.0, 
        ('OO', 'A'): 0.0,
        ('OO', 'AB'): 0.0, 
        ('OO', 'B'): 0.0, 
        ('OO', 'O'): 1.0})
    
def createInheritedGeneDist(genotypeVar, geneVar):
    V = Variable(genotypeVar, genotypes)
    W = Variable(geneVar, genes)
    return MultivariateFunction([V, W], {
        ('AA', 'A'): 1.0,
        ('AA', 'B'): 0.0, 
        ('AA', 'O'): 0.0, 
        ('AB', 'A'): 0.5,
        ('AB', 'B'): 0.5, 
        ('AB', 'O'): 0.0, 
        ('AO', 'A'): 0.5,
        ('AO', 'B'): 0.0, 
        ('AO', 'O'): 0.5, 
        ('BB', 'A'): 0.0,
        ('BB', 'B'): 1.0, 
        ('BB', 'O'): 0.0, 
        ('BO', 'A'): 0.0,
        ('BO', 'B'): 0.5, 
        ('BO', 'O'): 0.5, 
        ('OO', 'A'): 0.0,
        ('OO', 'B'): 0.0, 
        ('OO', 'O'): 1.0})
    
def createSynthesizedGenotypeDist(motherGeneVar, fatherGeneVar, genotypeVar):
    V = Variable(motherGeneVar, genes)
    W = Variable(fatherGeneVar, genes)
    X = Variable(genotypeVar, genotypes)
    return MultivariateFunction([V, W, X], {
        ('A', 'A', 'AA'): 1.0,
        ('A', 'A', 'AB'): 0.0,
        ('A', 'A', 'AO'): 0.0,
        ('A', 'A', 'BB'): 0.0,
        ('A', 'A', 'BO'): 0.0,
        ('A', 'A', 'OO'): 0.0,
        ('A', 'B', 'AA'): 0.0,
        ('A', 'B', 'AB'): 1.0,
        ('A', 'B', 'AO'): 0.0,
        ('A', 'B', 'BB'): 0.0,
        ('A', 'B', 'BO'): 0.0,
        ('A', 'B', 'OO'): 0.0,
        ('A', 'O', 'AA'): 0.0,
        ('A', 'O', 'AB'): 0.0,
        ('A', 'O', 'AO'): 1.0,
        ('A', 'O', 'BB'): 0.0,
        ('A', 'O', 'BO'): 0.0,
        ('A', 'O', 'OO'): 0.0,
        ('B', 'A', 'AA'): 0.0,
        ('B', 'A', 'AB'): 1.0,
        ('B', 'A', 'AO'): 0.0,
        ('B', 'A', 'BB'): 0.0,
        ('B', 'A', 'BO'): 0.0,
        ('B', 'A', 'OO'): 0.0,
        ('B', 'B', 'AA'): 0.0,
        ('B', 'B', 'AB'): 0.0,
        ('B', 'B', 'AO'): 0.0,
        ('B', 'B', 'BB'): 1.0,
        ('B', 'B', 'BO'): 0.0,
        ('B', 'B', 'OO'): 0.0,
        ('B', 'O', 'AA'): 0.0,
        ('B', 'O', 'AB'): 0.0,
        ('B', 'O', 'AO'): 0.0,
        ('B', 'O', 'BB'): 0.0,
        ('B', 'O', 'BO'): 1.0,
        ('B', 'O', 'OO'): 0.0,
        ('O', 'A', 'AA'): 0.0,
        ('O', 'A', 'AB'): 0.0,
        ('O', 'A', 'AO'): 1.0,
        ('O', 'A', 'BB'): 0.0,
        ('O', 'A', 'BO'): 0.0,
        ('O', 'A', 'OO'): 0.0,
        ('O', 'B', 'AA'): 0.0,
        ('O', 'B', 'AB'): 0.0,
        ('O', 'B', 'AO'): 0.0,
        ('O', 'B', 'BB'): 0.0,
        ('O', 'B', 'BO'): 1.0,
        ('O', 'B', 'OO'): 0.0,
        ('O', 'O', 'AA'): 0.0,
        ('O', 'O', 'AB'): 0.0,
        ('O', 'O', 'AO'): 0.0,
        ('O', 'O', 'BB'): 0.0,
        ('O', 'O', 'BO'): 0.0,
        ('O', 'O', 'OO'): 1.0})

def exampleBloodtypeNetwork():    
    fRdot = createGenotypePrior('Rdot')
    fSdot = createGenotypePrior('Sdot')
    fM = createInheritedGeneDist('Rdot', 'M')
    fF = createInheritedGeneDist('Sdot', 'F')
    fTdot = createSynthesizedGenotypeDist('M', 'F', 'Tdot')
    fR = createBloodtypeDist('Rdot', 'R')
    fS = createBloodtypeDist('Sdot', 'S')
    fT = createBloodtypeDist('Tdot', 'T')
    return BayesianNetwork([fRdot, fSdot, fR, fS, fT, fM, fF, fTdot])

def test():
    bnet = exampleBloodtypeNetwork()
    result = conditionalProb(bnet, {'R': 'AB'}, {'T': 'A'})
    print("""The probability that Rhonda has bloodtype AB, given that 
          Tim has blood type A, is: {}""".format(result))

if __name__ == "__main__":
    test()