sentence = input("Введіть речення: ")

words = sentence.split(" ")

count = 0
for word in words:
  if word.lower().startswith('н'):
    count += 1

print("Кількість слів, що починаються з літери 'н':", count)
