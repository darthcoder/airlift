import sympy

sympy.init_printing(use_unicode=True)

c0, c1, c2, c3, c4, c5, c6 = sympy.symbols("C_0 C_1 C_2 C_3 C_4 C_5 C_6")
x, y = sympy.symbols("x y")

left = x ** 2 + 2*x + (c1 - c2)
right = x + y - (c5 * c6)

the_equation = sympy.Eq(left, right)

sympy.solveset(the_equation, x)