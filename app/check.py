import numpy as np

print(np.__version__)

import sympy

c = sympy.symbols('c1 c2 c3 c4 c5 c6')
M = sympy.Matrix([
  [0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0],
  [1, 1, 0, 1, 0, 0],
  [1, 1, 0, -1, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 0, 1, 0, 0],
])

u = sympy.zeros(6, 1)

system = M, u

c = sympy.linsolve(system)

print(type(c))

for ci in c:
  for cj in ci:
    if type(cj) is sympy.core.symbol.Symbol:
      print(f"{cj} is symbol")
    else:
      print(f"{cj} is value")
