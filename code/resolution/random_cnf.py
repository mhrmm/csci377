import random

from cnf import Literal, Clause
from resolution import resolution_solver

def choose(N, k):
    numbers = list(range(N))
    random.shuffle(numbers)
    return numbers[:k]

def generate_random_clause(k, N):
    variables = choose(N, k)
    literals = []
    for var in variables:
        neg = random.choice([True,False])
        literal = Literal(str(var), neg)
        literals.append(literal)
    return Clause(literals)

def generate_random_cnf(k_sat, num_symbols, num_clauses):
    return [generate_random_clause(k_sat, num_symbols) for i in range(num_clauses)]

def plot_random_cnf(k_sat, num_symbols, max_num_clauses, step_size, num_trials):
    """
    Example usage:
        
    import matplotlib.pyplot as plt
    from random_cnf import plot_random_cnf
    (x,y) = plot_random_cnf(3,5,150,10,50)
    plt.plot(x,y)
    
    """
    x_values = []
    y_values = []
    for l in range(1, max_num_clauses, step_size):
        satisfiable_count = 0
        for trial in range(num_trials):
            if resolution_solver(generate_random_cnf(k_sat, num_symbols, l)):
                satisfiable_count += 1
        x_values.append(l)
        y_values.append(satisfiable_count / num_trials)
    return x_values, y_values
                

