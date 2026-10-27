from history import remember, show
from utils import add, sub, mul

print("Калькулятор")
print("2 + 3 =", add(2, 3))
print("7 - 4 =", sub(7, 4))
print("3 * 5 =", mul(3, 5))
print("Готово")
remember("2 + 3 = 5")
show()
