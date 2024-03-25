def remove_duplicates(input_list):
  return list(set(input_list))

input_list = list(map(int, input("Введіть список чисел: ").split()))

print("Початковий список:")
print(input_list)

unique_list = remove_duplicates(input_list)

print("Список після видалення елементів, що повторюються:")
print(unique_list)
