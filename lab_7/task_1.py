students = {
  "Vitaly_Prikhodko": {"first_name": "Віталій", "last_name": "Приходько", "middle_name": "Миколайович", "birthdate": (2004, 25, 10), "grades": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10]},
  "Dmytro_Kropyvnytskyi": {"first_name": "Дмитро", "last_name": "Кропивницький", "middle_name": "Андрійович", "birthdate": (2003, 5, 12), "grades": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4]},
  "Mikhail_Romanenko": {"first_name": "Михайло", "last_name": "Романенко", "middle_name": "Ігорович", "birthdate": (2005, 11, 5), "grades": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4]},
  "Maxim_Derizemlya": {"first_name": "Максим", "last_name": "Деріземля", "middle_name": "Олександрович", "birthdate": (2002, 8, 7), "grades": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7]},
  "Victoria_Zhuk": {"first_name": "Вікторія", "last_name": "Жук", "middle_name": "Олександрівна", "birthdate": (2006, 4, 3), "grades": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12]},
  "Andrey_Kuryanov": {"first_name": "Андрій", "last_name": "Кур'янов", "middle_name": "Юрійович", "birthdate": (2005, 8, 7), "grades": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8]},
  "Oksana_Dubovets": {"first_name": "Оксана", "last_name": "Дубовець", "middle_name": "Василівна", "birthdate": (2007, 11, 10), "grades": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10]},
  "Nikita_Stroganov": {"first_name": "Микита", "last_name": "Строганов", "middle_name": "Іванович", "birthdate": (2000, 2, 8), "grades": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9]},
  "Karina_Nikolaenko": {"first_name": "Карина", "last_name": "Ніколаєнко", "middle_name": "Петрівна", "birthdate": (2004, 22, 9), "grades": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8]},
  "Eugenia_Dron": {"first_name": "Євгенія", "last_name": "Дрон", "middle_name": "Сергіївна", "birthdate": (2001, 11, 11), "grades": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8]}
}

def print_students(students):
  print("Список учнів та їх оцінки:")
  for key, data in students.items():
    full_name = f"{data['last_name']} {data['first_name']} {data['middle_name']}"
    grades = data['grades']
    print(f"Ключ: {key}, {full_name}: {grades}")

def add_student(students, key, first_name, last_name, middle_name, birthdate, grades):
  if key in students:
    print(f"Студент {first_name} {middle_name} {last_name} вже є у базі.")
  else:
    students[key] = {"first_name": first_name, "last_name": last_name, "middle_name": middle_name, "birthdate": birthdate, "grades": grades}
    print(f"Студента {first_name} {middle_name} {last_name} було успішно додано.")

def remove_student(students, key):
  if key in students:
      del students[key]
      print(f"Студент {key} був видалений зі списку.")
  else:
      print(f"Студента {key} немає у списку.")

def find_students_with_birthday_today(students):
  date_input = input("Введіть дату у форматі 'день місяць': ")
  day, month = map(int, date_input.split())
  today = (day, month)
  print("Студенти з днем народження сьогодні:")
  for name, data in students.items():
      if data['birthdate'][1:] == today[0:]:
          print(f"{data['last_name']} {data['first_name']} {data['middle_name']}")

while True:
  print("\nВиберіть опцію:")
  print("1. Переглянути список учнів")
  print("2. Додати нового учня")
  print("3. Видалити учня")
  print("4. Знайти учнів з днем народження сьогодні")
  print("5. Вийти")

  choice = input("Ваш вибір: ")

  if choice == '1':
    print_students(students)
  elif choice == '2':
    key = input("Введіть ключ для нового учня: ")
    first_name = input("Введіть ім'я учня: ")
    last_name = input("Введіть прізвище учня: ")
    middle_name = input("Введіть по-батькові учня: ")
    birthdate = tuple(map(int, input("Введіть дату народження учня у форматі 'рік місяць день', розділену пробілами: ").split()))
    grades = list(map(int, input("Введіть оцінки учня, розділені пробілами: ").split()))
    add_student(students, key, first_name, last_name, middle_name, birthdate, grades)
  elif choice == '3':
    key = input("Введіть ключ учня, якого потрібно видалити: ")
    remove_student(students, key)
  elif choice == '4':
    find_students_with_birthday_today(students)
  elif choice == '5':
    print("До побачення!")
    break
  else:
    print("Невірний вибір. Спробуйте ще раз.")
