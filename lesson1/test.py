import sympy
p = list(sympy.primerange(1, 100))
print(p)

list1 = []
i = 0
for i in range(1, 100):
    list1.at[i] = i + 1

print(list1)