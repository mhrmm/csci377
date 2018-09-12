
def l(s):
    if s[0] == '!':
        return Literal(s[1:], True)
    else:
        return Literal(s, False)



def c(s):
    """
    Convenience method for constructing CNF clauses, e.g. for Exercise 7.12:
    
    c0 = c('a || b') 
    c1 = c('!a || b || e')        
    c2 = c('a || !b')        
    c3 = c('b || !e')        
    c4 = c('d || !e')        
    c5 = c('!b || !c || !f')        
    c6 = c('a || !e')        
    c7 = c('!b || f')        
    c8 = c('!b || c')        
    
    """
    literal_strings = [x.strip() for x in s.split('||')]
    return Clause([l(x) for x in literal_strings])


class Literal:
    def __init__(self, symbol, neg=False):
        self.symbol = symbol
        self.neg  = neg
    
    def __eq__(self, other):
        return self.symbol == other.symbol and self.neg == other.neg

    def __hash__(self):
        return hash(self.symbol) + hash(self.neg)
    
    def __str__(self):
        result = ''
        if self.neg:
            result = '!'
        return result + self.symbol
 
class Clause:
    def __init__(self, literals):
        self.literals = literals
        self.literal_values = dict()
        for lit in self.literals:
            self.literal_values[lit.symbol] = lit.neg

    def symbol_value(self, sym):
        if sym in self.literal_values:
            if self.literal_values[sym] == True:
                return -1
            else:
                return 1
        else:
            return 0
        
    def size(self):
        return len(self.literals)
        
    def symbols(self):
        return set([l.symbol for l in self.literals])
    
    def is_false(self):
        return len(self.literals) == 0
    
    def disjoin(self, clause):
        common_symbols = set(self.literal_values.keys()) & set(clause.literal_values.keys())
        for sym in common_symbols:
            if self.symbol_value(sym) * clause.symbol_value(sym) == -1:
                return None
        return Clause(list(set(self.literals + clause.literals)))

    def remove(self, sym):
        new_literals = set(self.literals) - set([Literal(sym, False), Literal(sym, True)])
        return Clause(list(new_literals))

    def __eq__(self, other):
        return set(self.literals) == set(other.literals)

    def __lt__(self, other):
        return str(self) < str(other)

    def __hash__(self):
        return hash(tuple(sorted([str(l) for l in self.literals])))

      
    def __str__(self):
        if len(self.literals) == 0:
            return 'FALSE'
        else:
            return ' || '.join([str(l) for l in self.literals])

 