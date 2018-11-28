

class Variable:    
    """A variable and its domain."""
    
    def __init__(self, name, domain):
        self._name = name
        self._domain = tuple(domain)
        
    def getName(self):
        return self._name
    
    def getDomain(self):
        return self._domain
    
    def __hash__(self):
        return hash(self._name)
    
    def __str__(self):
        return self._name
    
    def __eq__(self, other):
        return other._name == self._name and other._domain == self._domain
    
def instantiations(variables):
    """
    Takes a list of variables and returns the cross-product of the domains.
    
    For instance, suppose the domain of variable X is ('a', 'b') and the
    domain of the variable Y is ('c','d','e'). Then:
        
       >>> X = Variable('X', ('a', 'b'))
       >>> Y = Variable('Y', ('c', 'd', 'e'))
       >>> instantiations([X, Y])
       [('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    
    """
    def instantiationsHelper(variables):
        if len(variables) == 0:
            return [()]
        if len(variables) == 1:
            return [[v] for v in variables[0].getDomain()]
        else:
            firstVar = variables[0]
            otherInstantiations = instantiationsHelper(variables[1:])
            result = []
            for value in firstVar.getDomain():
                for inst in otherInstantiations:
                    result.append([value] + inst)
            return result
    return [tuple(i) for i in instantiationsHelper(variables)]
    