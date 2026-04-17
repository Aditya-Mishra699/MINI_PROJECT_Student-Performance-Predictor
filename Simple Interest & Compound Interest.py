# calcualte simple interest and compound interest

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

SI = (p * r * t) / 100

CI = p * (1 + r/100) ** t - p

print("Simple Interest =", SI)
print("Compound Interest =", CI)