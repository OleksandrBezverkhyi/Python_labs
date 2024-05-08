import json
import os

initial_data = [
    {"Name": "Vasyl", "Surname": "Logvinov", "Patronymic": "Antonovych", "Birthdate": "1999-05-15", "Gender": "Male"},
    {"Name": "Anton", "Surname": "Lypovyi", "Patronymic": "Andriiovych", "Birthdate": "2000-08-20", "Gender": "Male"},
    {"Name": "Alina", "Surname": "Popovych", "Patronymic": "Viktorivna", "Birthdate": "2001-11-25", "Gender": "Female"},
    {"Name": "Ivan", "Surname": "Petrenko", "Patronymic": "Oleksandrovych", "Birthdate": "1998-03-10", "Gender": "Male"},
    {"Name": "Maria", "Surname": "Ivanova", "Patronymic": "Serhiivna", "Birthdate": "1997-07-08", "Gender": "Female"},
    {"Name": "Oleksiy", "Surname": "Kovalchuk", "Patronymic": "Andriiovych", "Birthdate": "2002-08-18", "Gender": "Male"},
    {"Name": "Natalia", "Surname": "Sydorenko", "Patronymic": "Oleksandrivna", "Birthdate": "2003-12-05", "Gender": "Female"},
    {"Name": "Vitaliy", "Surname": "Pavlenko", "Patronymic": "Ihorovych", "Birthdate": "1995-04-30", "Gender": "Male"},
    {"Name": "Yulia", "Surname": "Hryhorova", "Patronymic": "Vitaliivna", "Birthdate": "2004-08-22", "Gender": "Female"},
    {"Name": "Oleg", "Surname": "Zaitsev", "Patronymic": "Mykhailovych", "Birthdate": "2001-06-12", "Gender": "Male"}
]

if not os.path.exists("Data.json"):
    with open("Data.json", "w") as file:
        json.dump(initial_data, file)
        print("Файл 'Data.json' був створений та дані були записані в нього.")

def read_json_objects(filename):
    with open(filename, "r") as file:
        objects = json.load(file)
    return objects

def write_json_objects(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

while True:
    print("\nОберіть дію:\n 1 - Додати дані\n 2 - Переглянути дані\n 3 - Знайти студентів з днями народження у вказаному місяці\n 4 - Видалити студента\n 5 - Вийти")
    choice = input("Виберіть варіант: ")

    if choice == '1':
        with open("Data.json", "r+") as file:
            data = json.load(file)
            new_student = {
                "Name": input("Ім'я: "),
                "Surname": input("Прізвище: "),
                "Patronymic": input("По-батькові: "),
                "Birthdate": input("Дата народження (РРРР-ММ-ДД): "),
                "Gender": input("Стать: ")
            }
            data.append(new_student)
            file.seek(0) 
            json.dump(data, file)
            print("Дані успішно додано!")

    elif choice == '2':
        data = read_json_objects("Data.json")
        print("Дані про студентів:")
        for student in data:
            print(student)

    elif choice == '3':
        month = input("Введіть місяць (ММ): ")
        data = read_json_objects("Data.json")
        birthdays = [student for student in data if student["Birthdate"].split("-")[1] == month]
        if birthdays:
            print("Студенти, чиї дні народження припадають на цей місяць:")
            for student in birthdays:
                print(f"{student['Name']} {student['Surname']}")
            with open("Dates.json", "w") as file:
                json.dump(birthdays, file)
                print("Дані про студентів з днями народження у вказаному місяці були записані у файл 'Dates.json'.")
        else:
            print("У цьому місяці не знайдено жодного студента, який би мав день народження.")

    elif choice == '4':
        first_name = input("Введіть ім'я студента: ")
        last_name = input("Введіть прізвище студента: ")
        patronymic = input("Введіть по-батькові студента: ")
        data = read_json_objects("Data.json")
        updated_data = [student for student in data if (student["Name"] != first_name or student["Surname"] != last_name or student["Patronymic"] != patronymic)]
        if len(updated_data) < len(data):
            write_json_objects("Data.json", updated_data)
            print("Студент видалений!")
        else:
            print("Студент не знайдений.")

    elif choice == '5':
        print("Вихід...")
        break

    else:
        print("Неправильний вибір. Будь ласка, виберіть ще раз.")
