import math
from mod import required_money

def calc(alpha):
  return pow(math.cos(alpha), 2) + pow(math.cos(alpha), 4) 

alpha = float(input("Введіть значення α: "))

print(f"Значення виразу cos^2(α) + cos^4(α) = ", format(calc(alpha), '.3f'))

stipend = float(input("\nВведіть суму щомісячної стипендії: "))
expenses = float(input("Введіть початкові щомісячні витрати: "))

required_money_amount = required_money(stipend, expenses)
if required_money_amount <= 0:
  print("Ви можете обійтись без додаткових коштів батьків.")
else:
  print(f"Потрібно попросити у батьків {required_money_amount:.2f} грн.")
