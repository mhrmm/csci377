def get_symbols(clauses):
    syms = set([])
    for clause in clauses:
        syms = syms | clause.symbols()
    return syms

def check_model_against_clause(model, clause):
    for symbol in clause.symbols():
        if model[symbol] == clause.symbol_value(symbol):
            return True
    return False

def check_model(model, clauses):
    for clause in clauses:
        if not check_model_against_clause(model, clause):
            return False
    return True

def assign(model_so_far, symbol, bool_assignment):
    if bool_assignment:
        assignment = 1
    else:
        assignment = -1
    return {**model_so_far, symbol: assignment}


def search_solver(clauses, verbose=False):
    """
    Example usage:
        
    from search import *
    from resolution import example_clauses
    search_solver(example_clauses)           [ should return False ]
    search_solver(example_clauses[1:])       [ should return True ]

    """    
    symbols = list(get_symbols(clauses))
    return _search_solver_helper(clauses, symbols, dict())
                
def _search_solver_helper(clauses, unassigned_symbols, m):
    if len(unassigned_symbols) == 0:
        return check_model(m, clauses)
    else:
        next_symbol = unassigned_symbols[0]
        satisfiable_if_true = _search_solver_helper(
                clauses, 
                unassigned_symbols[1:], 
                assign(m, next_symbol, True))
        return satisfiable_if_true or _search_solver_helper(
                clauses, 
                unassigned_symbols[1:], 
                assign(m, next_symbol, False))

