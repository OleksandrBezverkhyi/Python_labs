def open_file(file_name, mode):
  try:
    file = open(file_name, mode)
  except FileNotFoundError:
    print("Файл", file_name, "не знайдено!")
    return None
  except:
    print("Помилка відкриття файлу", file_name)
    return None
  else:
    print("Файл", file_name, "був відкритий успішно!")
    return file


def find_and_write_doubled_letters(input_file_name, output_file_name):
  input_file = open_file(input_file_name, "r")
  output_file = open_file(output_file_name, "w")

  if input_file and output_file:
    doubled_words_found = False
    for line in input_file:
      words = line.split()
      for word in words:
        doubled = False
        for i in range(len(word) - 1):
          if word[i] == word[i + 1]:
            doubled = True
            break
        if doubled:
          output_file.write(word + '\n')
          doubled_words_found = True

    if not doubled_words_found:
      output_file.write("Немає слів з подвоєнням букв.")

    input_file.close()
    output_file.close()
    print("Файли було успішно закрито!")


def print_file_content(file_name):
  file = open_file(file_name, "r")
  if file:
    print("Вміст файлу", file_name + ":")
    for line in file:
      print(line.strip())
    file.close()
    print("Файл", file_name, "було успішно закрито!")


input_file_name = "TF7_1.txt"
output_file_name = "TF7_2.txt"

file_1_w = open_file(input_file_name, "w")
if file_1_w:
  file_1_w.write(
      "Текст без подвоєнь"
  )
  print("Інформація була успішно додана до", input_file_name + "!")
  file_1_w.close()

find_and_write_doubled_letters(input_file_name, output_file_name)
print_file_content(output_file_name)
