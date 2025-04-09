# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:32:22 2025

@author: sam77
"""

import numpy as np

def main():
    print("Enter values of random variable X (e.g., 0, 1, 2):")
    X = list(map(int, input().split()))
    
    print("Enter corresponding probabilities P(X) (e.g., 0.25 0.5 0.25):")
    P = list(map(float, input().split()))

    if len(X) != len(P) or not np.isclose(sum(P), 1.0):
        print("Error: X and P must be same length and probabilities must sum to 1.")
        return

    # PMF
    pmf = dict(zip(X, P))
    print(f"\nPMF: {pmf}")

    # CDF
    cdf = {}
    cumulative = 0
    for x, p in sorted(zip(X, P)):
        cumulative += p
        cdf[x] = cumulative
    print(f"CDF: {cdf}")

    # Expected Value E[X]
    EX = sum(x*p for x, p in zip(X, P))
    print(f"E[X]: {EX}")

    # Variance Var(X)
    EX2 = sum((x**2)*p for x, p in zip(X, P))
    VarX = EX2 - EX**2
    print(f"Var(X): {VarX}")

    # Standard Deviation
    std = np.sqrt(VarX)
    print(f"Standard Deviation: {std}")

    # E[X^2 + 5X + 6]
    expr1 = sum((x**2 + 5*x + 6)*p for x, p in zip(X, P))
    print(f"E[X^2 + 5X + 6]: {expr1}")

    # E[X^2 + bX]
    b = float(input("\nEnter value of b for E[X^2 + bX]: "))
    expr2 = sum((x**2 + b*x)*p for x, p in zip(X, P))
    print(f"E[X^2 + {b}X]: {expr2}")

    # Var(5X)
    Var5X = 25 * VarX
    print(f"Var(5X): {Var5X}")

    # Var(2X + 10)
    Var2X_10 = 4 * VarX
    print(f"Var(2X + 10): {Var2X_10}")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
###################################3
#######################################
    
    
def main():
    print("Enter values of random variable X (e.g., 0, 1, 2):")
    X = list(map(int, input().split()))
    
    print("Enter corresponding probabilities P(X) (e.g., 0.25 0.5 0.25):")
    P = list(map(float, input().split()))

    if len(X) != len(P) or sum(P) != 1.0:
        print("Error: X and P must be same length and probabilities must sum to 1.")
        return

    # PMF
    pmf = dict(zip(X, P))
    print(f"\nPMF: {pmf}")

    # CDF
    cdf = {}
    cumulative = 0
    for x, p in sorted(zip(X, P)):
        cumulative += p
        cdf[x] = cumulative
    print(f"CDF: {cdf}")

    # Expected Value E[X]
    EX = sum(x * p for x, p in zip(X, P))
    print(f"E[X]: {EX}")

    # Variance Var(X)
    EX2 = sum((x ** 2) * p for x, p in zip(X, P))
    VarX = EX2 - EX ** 2
    print(f"Var(X): {VarX}")

    # Standard Deviation
    std = (VarX) ** 0.5
    print(f"Standard Deviation: {std}")

    # E[X^2 + 5X + 6]
    expr1 = sum((x ** 2 + 5 * x + 6) * p for x, p in zip(X, P))
    print(f"E[X^2 + 5X + 6]: {expr1}")

    # E[X^2 + bX]
    b = float(input("\nEnter value of b for E[X^2 + bX]: "))
    expr2 = sum((x ** 2 + b * x) * p for x, p in zip(X, P))
    print(f"E[X^2 + {b}X]: {expr2}")

    # Var(5X)
    Var5X = 25 * VarX
    print(f"Var(5X): {Var5X}")

    # Var(2X + 10)
    Var2X_10 = 4 * VarX
    print(f"Var(2X + 10): {Var2X_10}")

if __name__ == "__main__":
    main()
