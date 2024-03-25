def find_first_five_min():
  input_list = list(map(int, input("Введіть список чисел: ").split()))

  min_elements = sorted(input_list)[:5]

  print("Перші п'ять мінімальних елементів:", min_elements)

find_first_five_min()
