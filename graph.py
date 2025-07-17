
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Step 1: Input function as string
equation_input = input("Enter an equation in x (e.g., x**2 - 4*x + 3 or sin(x)): ")

# Step 2: Convert string to symbolic expression
x = sp.symbols('x')
try:
    expr = sp.sympify(equation_input)
except sp.SympifyError:
    print("Invalid equation!")
    exit()

# Step 3: Convert symbolic expression to a Python function
f = sp.lambdify(x, expr, modules=['numpy'])

# Step 4: Create x values and evaluate the function
x_vals = np.linspace(-10, 10, 1000)
try:
    y_vals = f(x_vals)
except:
    print("Error evaluating the function.")
    exit()

# Step 5: Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=f"f(x) = {expr}", color='blue')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.title("Graph of f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

