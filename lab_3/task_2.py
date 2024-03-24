word = input("Введіть слово: ")

seen = set()
duplicates = []

for letter in word:
  if letter in seen:
    duplicates.append(letter)
  else:
    seen.add(letter)

if duplicates:
  print("Дубльовані літери у слові:", ', '.join(duplicates))
else:
  print("У слові немає дубльованих літер.")
