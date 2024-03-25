def operate_sets(A, x):
  if x not in A:
      A.add(x)
      print(f"Символ '{x}' був доданий до множини A:", A)
  else:
      A.remove(x)
      print(f"Символ '{x}' був видалений з множини A:", A)
  return A

A = set(input("Введіть множину символів: ").split())

x = input("Введіть символ x: ")

result_set = operate_sets(A, x)
print("Результат множини B:", result_set)
