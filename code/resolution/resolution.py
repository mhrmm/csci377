import queue

def resolve_symbol(clause1, clause2, symbol):
    if clause1.symbol_value(symbol) * clause2.symbol_value(symbol) == -1:
        return clause1.remove(symbol).disjoin(clause2.remove(symbol))
    return None

def resolve(clause1, clause2):
    resolvents = []
    for sym in clause1.symbols() & clause2.symbols():
       resolvent = resolve_symbol(clause1, clause2, sym)  
       if resolvent is not None:
           resolvents.append(resolvent)
    return resolvents


class ClauseQueue:
    def __init__(self, queue = queue.Queue(), priority_function = lambda clause: 0):
        self.queue = queue
        self.priority_function = priority_function
        self.cached_clauses = set([])
        
    def push(self, clause):
        if not clause in self.cached_clauses:
            self.queue.put((self.priority_function(clause), clause))
            self.cached_clauses.add(clause)
            return True
        else:
            return False
    
    def pop(self):
        return self.queue.get()[1]
    
    def empty(self):
        return self.queue.empty()
    
    def numGenerated(self):
        return len(self.cached_clauses)


def resolution_solver(clauses, verbose=False):
    """
    Example usage:
        
    from resolution import *
    resolution_solver(example_clauses, verbose=True)     [ should return False ]
    resolution_solver(example_clauses[1:], verbose=True) [ should return True ]

    """
    processed = set([])
    unprocessed = ClauseQueue(queue.PriorityQueue(), lambda clause: clause.size())
    for c in clauses:
        unprocessed.push(c)
    while not unprocessed.empty():
        next_to_process = unprocessed.pop()
        for clause in processed:
            for resolvent in resolve(next_to_process, clause):
                is_new_clause = unprocessed.push(resolvent)
                if is_new_clause and verbose:
                    print("{} [BY RESOLVING {} WITH {}]"
                          .format(resolvent, next_to_process, clause))                    
                if resolvent.is_false():
                    if verbose:
                        print("Proved unsat after generating {} clauses."
                              .format(unprocessed.numGenerated()))
                    return False
        processed.add(next_to_process)
    if verbose:
        print("Proved sat after generating {} clauses."
              .format(unprocessed.numGenerated()))
    return True

import cnf
example_clauses = [cnf.c('a || b'), 
                   cnf.c('!a || b || e'),
                   cnf.c('a || !b'),
                   cnf.c('b || !e') ,
                   cnf.c('d || !e'),
                   cnf.c('!b || !c || !f'),
                   cnf.c('a || !e'),
                   cnf.c('!b || f'),
                   cnf.c('!b || c')]
