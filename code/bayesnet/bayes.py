from variable import instantiations

class MultivariateFunction:    
    def __init__(self, variables, values):
        self._variables = variables
        self._values = values
    
    def getVariables(self):
        return self._variables
    
    def getValue(self, instantiation):
        key = []
        for var in self._variables:
            if var.getName() not in instantiation:
                print(instantiation)
                print([v.getName() for v in self._variables])
                raise Exception('Variable {} not found in given instantiation.'.format(var))
            key.append(instantiation[var.getName()])
        return self._values[tuple(key)]
    
    def sumOut(self, variable):
        if variable not in self._variables:
            raise Exception('Variable {} not found.'.format(variable))
        else:
            variableIndex = self._variables.index(variable)
            otherVariables = self._variables[0:variableIndex] + self._variables[variableIndex + 1:]
            newValues = dict()
            for inst in instantiations(otherVariables):
                result = 0.0
                for value in variable.getDomain():
                    lookupInst = inst[0:variableIndex] + (value,) + inst[variableIndex:]
                    result += self._values[lookupInst]
                newValues[inst] = result
            return MultivariateFunction(otherVariables, newValues)
  

def multiply(fns):
    def convertInstantiationToDict(inst, variables):
        result = dict()
        for (var, value) in zip(variables, inst):
            result[var.getName()] = value
        return result
    allVars = set()
    for fn in fns:
        allVars = allVars | set(fn.getVariables())
    allVars = list(allVars)
    values = dict()
    for inst in instantiations(allVars):
        product = 1.0
        instDict = convertInstantiationToDict(inst, allVars)
        for fn in fns:
            product *= fn.getValue(instDict)
        values[inst] = product
    return MultivariateFunction(allVars, values)
        

class BayesianNetwork:
    
    def __init__(self, factors):
        self._factors = factors
        self._variables = set()
        for factor in factors:
            self._variables = self._variables | set(factor.getVariables())
        
    def getFactorsWithVariable(self, variable):
        return [factor for factor in self._factors 
                if variable in factor.getVariables()]

    def getVariables(self):
        return self._variables

    def eliminate(self, variable):
        relevant = []
        irrelevant = []
        for factor in self._factors:
            if variable in factor.getVariables():
                relevant.append(factor)
            else:
                irrelevant.append(factor)
        newFactor = multiply(relevant)
        newFactor = newFactor.sumOut(variable)
        return BayesianNetwork(irrelevant + [newFactor])
    
    def getValue(self, instantiation):
        g = multiply(self._factors)
        return g.getValue(instantiation)
    
        
def variableElim(bnet, evidence):
    allVars = bnet.getVariables()
    marginalizedVariables = [v for v in allVars 
                             if v.getName() not in evidence.keys()]    
    for var in marginalizedVariables:    
        bnet = bnet.eliminate(var)
    return bnet.getValue(evidence)
    
def conditionalProb(bnet, event, evidence):
    eventAndEvidence = {**event, **evidence}
    return variableElim(bnet, eventAndEvidence) / variableElim(bnet, evidence)
        
